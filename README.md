## Objective
See instructions [here][instructions].

## Execution
Running `docker-compose up` will:
- Create api server container
- Create test container
- Execute all tests in test container
- Produce test report [here][test report]
- Keep both containers running for any debugging or re-running of tests

## Design
Tests are executed in parallel, split in 3 workers, according to file.

In essence, each worker handles a suite:
- positive cases
- negative cases
- load testing  

This affects load testing, since other concurrent tests slow down server, and can be avoided by setting 
`-n=3` to `-n=0` in test [dockerfile][test dockerfile].


[instructions]: instructions.md
[test report]: test/test_reports/report.htm
[test dockerfile]: test/Dockerfile