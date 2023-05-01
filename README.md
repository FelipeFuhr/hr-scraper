# HR Scraper
![version](badges/version.svg)
![coverage](badges/coverage.svg)

An implementation of a scraper .

### Run
Steps to run:
### 0. Have a working kubernetes cluster and a container runtime installed
### 1. Build images:
```
make build
```
### 2. Run kubernetes resources:
```
make apply
```

### Installation

To install only the package locally:
```
make pkg
```

To install everything (including dev dependencies):
```
make install
```

### Utils
To make a general check on the files. After it runs, if it is successful, you should be in a state that you are ready to commit.
```
make check
```

To run static analysis and formatting:
```
make check-format
```

To run unit tests:
```
make test
```

To generate badges:
```
make badge
```

To build docs:
```
make build-docs
```

To clean up:
```
make clean
```
