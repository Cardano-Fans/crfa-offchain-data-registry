#!/usr/bin/env python3
"""
JSON Schema validation script for CRFA offchain data registry.
This script validates all JSON files in the dApps directory against the schema.
"""

import json
import os
import sys
from pathlib import Path
from jsonschema import validate, ValidationError, Draft7Validator

def load_json_file(file_path):
    """Load and parse a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in {file_path}: {e}")
        return None
    except Exception as e:
        print(f"❌ Error reading {file_path}: {e}")
        return None

def validate_dapp_file(file_path, schema):
    """Validate a single dApp JSON file against the schema."""
    print(f"🔍 Validating {file_path}...")
    
    data = load_json_file(file_path)
    if data is None:
        return False
    
    try:
        validate(instance=data, schema=schema)
        print(f"✅ {file_path} is valid")
        return True
    except ValidationError as e:
        print(f"❌ {file_path} validation failed:")
        print(f"   Error: {e.message}")
        if e.path:
            print(f"   Path: {' -> '.join(str(p) for p in e.path)}")
        return False

def check_id_uniqueness(json_files):
    """Check if all dApp IDs are unique across all files."""
    print("🔍 Checking ID uniqueness...")
    
    id_to_file = {}
    duplicates = []
    
    for json_file in json_files:
        data = load_json_file(json_file)
        if data is None:
            continue
            
        dapp_id = data.get('id')
        if dapp_id:
            if dapp_id in id_to_file:
                duplicates.append({
                    'id': dapp_id,
                    'files': [id_to_file[dapp_id], json_file.name]
                })
            else:
                id_to_file[dapp_id] = json_file.name
    
    if duplicates:
        print("❌ Duplicate IDs found:")
        for dup in duplicates:
            print(f"   ID '{dup['id']}' used in: {' and '.join(dup['files'])}")
        return False
    else:
        print(f"✅ All {len(id_to_file)} IDs are unique")
        return True

def main():
    """Main validation function."""
    # Get the root directory of the repository
    root_dir = Path(__file__).parent.parent
    schema_file = root_dir / "dapp-schema.json"
    dapps_dir = root_dir / "dApps"
    
    print("🚀 Starting JSON schema validation...")
    print(f"📁 Schema file: {schema_file}")
    print(f"📁 dApps directory: {dapps_dir}")
    
    # Load the schema
    if not schema_file.exists():
        print(f"❌ Schema file not found: {schema_file}")
        sys.exit(1)
    
    schema = load_json_file(schema_file)
    if schema is None:
        print("❌ Failed to load schema file")
        sys.exit(1)
    
    # Validate the schema itself
    try:
        Draft7Validator.check_schema(schema)
        print("✅ Schema is valid")
    except Exception as e:
        print(f"❌ Schema validation failed: {e}")
        sys.exit(1)
    
    # Find all JSON files in the dApps directory
    if not dapps_dir.exists():
        print(f"❌ dApps directory not found: {dapps_dir}")
        sys.exit(1)
    
    json_files = list(dapps_dir.glob("*.json"))
    if not json_files:
        print("⚠️  No JSON files found in dApps directory")
        return
    
    print(f"📄 Found {len(json_files)} JSON files to validate")
    
    # Check ID uniqueness first
    ids_unique = check_id_uniqueness(json_files)
    
    # Validate each file against schema
    valid_files = 0
    invalid_files = 0
    
    for json_file in sorted(json_files):
        if validate_dapp_file(json_file, schema):
            valid_files += 1
        else:
            invalid_files += 1
    
    # Print summary
    print(f"\n📊 Validation Summary:")
    print(f"   ✅ Valid files: {valid_files}")
    print(f"   ❌ Invalid files: {invalid_files}")
    print(f"   📄 Total files: {len(json_files)}")
    print(f"   🆔 IDs unique: {'✅ Yes' if ids_unique else '❌ No'}")
    
    if invalid_files > 0 or not ids_unique:
        error_msg = []
        if invalid_files > 0:
            error_msg.append(f"{invalid_files} files have schema errors")
        if not ids_unique:
            error_msg.append("duplicate IDs found")
        
        print(f"\n❌ Validation failed! {' and '.join(error_msg)}.")
        sys.exit(1)
    else:
        print(f"\n🎉 All files are valid and all IDs are unique!")

if __name__ == "__main__":
    main()