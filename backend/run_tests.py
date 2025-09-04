#!/usr/bin/env python3
"""
Test runner script for the Louis Italian Restaurant project.
This script provides various testing options for the project.
"""

import sys
import os
import subprocess
import argparse

def run_tests(test_type="all", verbose=False, coverage=False, stop_on_fail=False):
    """Run pytest with specified options"""
    
    # Base pytest command
    cmd = ["python", "-m", "pytest"]
    
    # Add test path based on type
    if test_type == "controllers":
        cmd.append("src/test/controllers/")
    elif test_type == "views":
        cmd.append("src/test/views/")
    elif test_type == "validators":
        cmd.append("src/test/validators/")
    elif test_type == "models":
        cmd.append("src/test/models/")
    elif test_type == "all":
        cmd.append("src/test/")
    else:
        cmd.append(f"src/test/{test_type}")
    
    # Add options
    if verbose:
        cmd.append("-v")
    
    if coverage:
        cmd.extend(["--cov=src", "--cov-report=html", "--cov-report=term"])
    
    if stop_on_fail:
        cmd.append("-x")
    
    # Always add some useful options
    cmd.extend(["--tb=short", "--strict-markers"])
    
    print(f"Running command: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, cwd=os.path.dirname(os.path.abspath(__file__)))
        return result.returncode
    except KeyboardInterrupt:
        print("\nTests interrupted by user")
        return 1
    except Exception as e:
        print(f"Error running tests: {e}")
        return 1

def main():
    parser = argparse.ArgumentParser(description="Run tests for Louis Italian Restaurant project")
    parser.add_argument(
        "test_type", 
        nargs="?", 
        default="all",
        help="Type of tests to run: all, controllers, views, validators, models, or specific file path"
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    parser.add_argument("-c", "--coverage", action="store_true", help="Run with coverage")
    parser.add_argument("-x", "--stop-on-fail", action="store_true", help="Stop on first failure")
    
    args = parser.parse_args()
    
    exit_code = run_tests(
        test_type=args.test_type,
        verbose=args.verbose,
        coverage=args.coverage,
        stop_on_fail=args.stop_on_fail
    )
    
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
