import pytest

import logging
logging.basicConfig(level=logging.DEBUG)

from hpolib.container.benchmarks.nas.tabular_benchmarks import SliceLocalizationBenchmark, NavalPropulsionBenchmark, \
    ParkinsonsTelemonitoringBenchmark, ProteinStructureBenchmark


def setup():
    container_source = 'library://phmueller/automl/'
    benchmark = SliceLocalizationBenchmark(container_source=container_source)
    default_config = benchmark.get_configuration_space(seed=1).get_default_configuration()

    return container_source, default_config


def test_tabular_benchmark_wrong_input():
    container_source, default_config = setup()
    benchmark = SliceLocalizationBenchmark(container_source=container_source, rng=1)

    with pytest.raises(AssertionError):
        benchmark.objective_function(configuration=default_config, budget=0)

    with pytest.raises(ValueError):
        benchmark.objective_function(configuration=default_config, budget=1, run_index=0.1)

    with pytest.raises(AssertionError):
        benchmark.objective_function(configuration=default_config, budget=1, run_index=[4])

    with pytest.raises(AssertionError):
        benchmark.objective_function(configuration=default_config, budget=1, run_index=[])

    with pytest.raises(AssertionError):
        benchmark.objective_function(configuration=default_config, budget=1, run_index=-1)

    with pytest.raises(AssertionError):
        benchmark.objective_function(configuration=default_config, budget=1, run_index=4)

    with pytest.raises(AssertionError):
        benchmark.objective_function(configuration=default_config, budget=101, run_index=3)

    benchmark = None


def test_slice_benchmark():
    container_source, default_config = setup()

    benchmark = SliceLocalizationBenchmark(container_source=container_source, rng=1)
    result = benchmark.objective_function(configuration=default_config, budget=1, run_index=[0, 1, 2, 3])

    mean = 0.01828
    assert result['function_value'] == pytest.approx(mean, abs=0.0001)

    runs = result['info']['valid_rmse_per_run']
    calculated_mean = sum(runs) / len(runs)
    assert calculated_mean == pytest.approx(mean, abs=0.0001)

    runtime = 5.7750
    assert result['cost'] == pytest.approx(runtime, abs=0.0001)

    runtimes = result['info']['runtime_per_run']
    calculated_runtime = sum(runtimes) / len(runtimes)
    assert calculated_runtime == pytest.approx(runtime, abs=0.0001)
    benchmark = None


def test_naval_benchmark():
    container_source, default_config = setup()

    benchmark = NavalPropulsionBenchmark(container_source=container_source)
    result = benchmark.objective_function(configuration=default_config, budget=1, run_index=[0, 1, 2, 3])

    mean = 0.8928
    assert result['function_value'] == pytest.approx(mean, abs=0.0001)

    runs = result['info']['valid_rmse_per_run']
    calculated_mean = sum(runs) / len(runs)
    assert calculated_mean == pytest.approx(mean, abs=0.0001)

    runtime = 1.3119
    assert result['cost'] == pytest.approx(runtime, abs=0.0001)

    runtimes = result['info']['runtime_per_run']
    calculated_runtime = sum(runtimes) / len(runtimes)
    assert calculated_runtime == pytest.approx(runtime, abs=0.0001)
    benchmark = None


def test_protein_benchmark():
    container_source, default_config = setup()

    benchmark = ProteinStructureBenchmark(container_source=container_source, rng=1)
    result = benchmark.objective_function(configuration=default_config, budget=1, run_index=[0, 1, 2, 3])

    mean = 0.4474
    assert result['function_value'] == pytest.approx(mean, abs=0.0001)

    runs = result['info']['valid_rmse_per_run']
    calculated_mean = sum(runs) / len(runs)
    assert calculated_mean == pytest.approx(mean, abs=0.0001)

    runtime = 4.8105
    assert result['cost'] == pytest.approx(runtime, abs=0.0001)

    runtimes = result['info']['runtime_per_run']
    calculated_runtime = sum(runtimes) / len(runtimes)
    assert calculated_runtime == pytest.approx(runtime, abs=0.0001)
    benchmark = None


def test_parkinson_benchmark():
    container_source, default_config = setup()

    benchmark = ParkinsonsTelemonitoringBenchmark(container_source=container_source, rng=1)
    result = benchmark.objective_function(configuration=default_config, budget=1, run_index=[0, 1, 2, 3])

    mean = 0.7425
    assert result['function_value'] == pytest.approx(mean, abs=0.0001)

    runs = result['info']['valid_rmse_per_run']
    calculated_mean = sum(runs) / len(runs)
    assert calculated_mean == pytest.approx(mean, abs=0.0001)

    runtime = 0.6272
    assert result['cost'] == pytest.approx(runtime, abs=0.0001)

    runtimes = result['info']['runtime_per_run']
    calculated_runtime = sum(runtimes) / len(runtimes)
    assert calculated_runtime == pytest.approx(runtime, abs=0.0001)
    benchmark = None