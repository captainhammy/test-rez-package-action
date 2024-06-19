[![Tests](https://github.com/captainhammy/test-rez-package-action/actions/workflows/tests.yml/badge.svg)](https://github.com/captainhammy/test-rez-package-action/actions/workflows/tests.yml)

# Test Rez Package

This GitHub Action will test a [rez](https://github.com/AcademySoftwareFoundation/rez) package via the `rez test` command.

# Usage

```yaml
  - name: Test Package
    uses: captainhammy/test-rez-package-action@v1
```

## Inputs

The following optional input values can be used:

### test_name

The `test_name` input can be used to execute a specific package test. The default value is '**unit**'.

```yaml
  - name: Test Package
    uses: captainhammy/test-rez-package-action@v1
    with:
      test_name: foo

  # Would execute the following command
  # rez test {package name} foo
```

### package_root

The `package_root` input is used to define where to build from. By default, this is the current directory (.).

This input is a hack around the fact you **cannot** specify a `working-directory` on **uses** steps in GitHub Actions. 

```yaml
  - name: Build Package
    uses: captainhammy/test-rez-package-action@v1
    with:
      package_root: ./tests/test_package

  # Would execute the following command
  # cd ./tests/test_package
  # rez test test_package unit
```

# Dependencies

While this package has no direct dependencies, it must be run in an environment where the `rez` command is available. 
