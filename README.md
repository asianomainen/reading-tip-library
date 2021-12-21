# reading-tip-library
![GitHub Actions](https://github.com/asianomainen/reading-tip-library/workflows/CI/badge.svg)  
[![codecov](https://codecov.io/gh/asianomainen/reading-tip-library/branch/main/graph/badge.svg?token=IM4BJC00JG)](https://codecov.io/gh/asianomainen/reading-tip-library)

## Project report
[Link to project report](https://docs.google.com/document/d/1xAEykxp7c1_VvfG7exvA3oFjSuYkrG2kYzBhyz4gdYU/edit?usp=sharing)

## Installation and user guide

#### Install dependencies

```
poetry install
```

#### Run the program

```
poetry run invoke start
```

#### Run unit tests

```
poetry run invoke test
```

#### Run Robot tests

```
poetry run invoke robot
```

#### Run code coverage raport

```
poetry run invoke coverage
```

#### Generate code coverage report

```
poetry run invoke coverage-report
```

## Definition of Done
- Unit tests written and passing
- Robot framework tests written and passing
  - [Acceptance criteria](https://github.com/asianomainen/reading-tip-library/blob/main/src/tests/test.robot)
- CI build passing
- Code coverage at least 75%
- Code refactoring done
- Code passes pylint
- Code reviewed by peers
- Acceptance criteria met and documented in Robot-framework syntax
- Documentation updated when relevant

## Documentation
[Link to Backlog](https://docs.google.com/spreadsheets/d/1A3XL6Ixnftyqe45tI8JnFBjwFhiAg_5na4TVUxUSTFI/edit?usp=sharing)  
[Definition of Done](https://github.com/asianomainen/reading-tip-library/blob/main/Documentation/definitionofdone.md)
[Project report](https://docs.google.com/document/d/1xAEykxp7c1_VvfG7exvA3oFjSuYkrG2kYzBhyz4gdYU/edit?usp=sharing)
