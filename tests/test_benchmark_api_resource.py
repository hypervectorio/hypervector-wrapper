import hypervector


def test_benchmark():
    benchmarks = hypervector.Benchmark.list()
    assert isinstance(benchmarks[0], hypervector.Benchmark)