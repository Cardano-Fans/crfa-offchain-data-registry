#!/usr/bin/env python3
"""
Script to fix invalid IDs in JSON files and generate proper 8-character IDs.
"""

import json
import os
import random
import string
from pathlib import Path

def generate_random_id(length=8):
    """Generate a random alphanumeric ID of specified length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def get_existing_ids(dapps_dir):
    """Get all existing IDs from JSON files to avoid duplicates."""
    existing_ids = set()
    json_files = list(dapps_dir.glob("*.json"))
    
    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if 'id' in data and len(data['id']) == 8 and data['id'].isalnum():
                    existing_ids.add(data['id'])
        except:
            continue
    
    return existing_ids

def generate_unique_id(existing_ids, length=8):
    """Generate a unique ID that doesn't exist in the set."""
    while True:
        new_id = generate_random_id(length)
        if new_id not in existing_ids:
            existing_ids.add(new_id)
            return new_id

def fix_file_id(file_path, existing_ids):
    """Fix the ID in a specific file if it's invalid."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        current_id = data.get('id', '')
        
        # Check if ID is invalid (not 8 alphanumeric characters)
        if not (len(current_id) == 8 and current_id.isalnum()):
            new_id = generate_unique_id(existing_ids)
            old_id = current_id
            data['id'] = new_id
            
            # Write back to file with proper formatting
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            
            print(f"✅ Fixed {file_path.name}: '{old_id}' -> '{new_id}'")
            return True
        else:
            print(f"✅ {file_path.name}: ID '{current_id}' is already valid")
            return False
            
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False

def main():
    """Main function to fix all invalid IDs."""
    root_dir = Path(__file__).parent.parent
    dapps_dir = root_dir / "dApps"
    
    if not dapps_dir.exists():
        print(f"❌ dApps directory not found: {dapps_dir}")
        return
    
    print("🔍 Finding files with invalid IDs...")
    
    # Get all existing valid IDs
    existing_ids = get_existing_ids(dapps_dir)
    print(f"📊 Found {len(existing_ids)} existing valid IDs")
    
    # Find and fix files with invalid IDs
    json_files = list(dapps_dir.glob("*.json"))
    fixed_count = 0
    
    for json_file in sorted(json_files):
        if fix_file_id(json_file, existing_ids):
            fixed_count += 1
    
    print(f"\n📊 Summary:")
    print(f"   🔧 Fixed files: {fixed_count}")
    print(f"   📄 Total files: {len(json_files)}")

if __name__ == "__main__":
    main()