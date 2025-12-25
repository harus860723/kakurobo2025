#!/usr/bin/env bash
# SPDX-FileCopyrightText: 2025 Haruki Matsushita
# SPDX-License-Identifier: BSD-3-Clause
set -e

echo "Python version:"
python --version

echo "Running main.py"
python main.py

echo "Test finished successfully"
