#!/usr/bin/env python3
"""

import sys
import os
import subprocess
import xml.etree.ElementTree as ET
from datetime import datetime

def run_test(name, command):
    """Запускает один тест"""
    print(f"\nRunning: {name}")
    print(f"Command: {command}")
    
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            print("PASSED")
            return True
        else:
            print(f"FAILED (code: {result.returncode})")
            if result.stderr:
                error_msg = result.stderr[:200].replace('\n', ' ')
                print(f"Error: {error_msg}")
            return False
            
    except subprocess.TimeoutExpired:
        print("TIMEOUT (30s)")
        return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False

def main():
    print("Starting CI/CD Test Runner")
    
    # Проверяем наличие файлов
    if not os.path.exists('test.xml'):
        print("File not found: test.xml")
        sys.exit(1)
    
    # Парсим XML и запускаем тесты
    try:
        tree = ET.parse('test.xml')
        root = tree.getroot()
        tests = root.findall('test')
        
        if not tests:
            print("No tests found in XML file")
            sys.exit(0)
        
        print(f"Found {len(tests)} test(s)")
        
        start_time = datetime.now()
        passed = 0
        failed = 0
        
        # Запускаем все тесты
        for test in tests:
            name = test.get('name', 'Unnamed test')
            command = test.get('command', '').strip()
            
            if not command:
                print(f"Skipping '{name}': empty command")
                continue
            
            if run_test(name, command):
                passed += 1
            else:
                failed += 1
        
        # Выводим итоги
        duration = datetime.now() - start_time
        
        print(f"\n" + "="*40)
        print("TEST SUMMARY")
        print(f"Total: {passed + failed}")
        print(f"Passed: {passed}")
        print(f"Failed: {failed}")
        print(f"Duration: {duration.total_seconds():.2f}s")
        print("="*40)
        
        if failed > 0:
            print("Some tests failed!")
            sys.exit(1)
        else:
            print("All tests passed!")
            sys.exit(0)
            
    except ET.ParseError as e:
        print(f"XML parsing error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
