# HPOlib3

HPOlib3 is a library for hyperparameter optimization and black-box optimization benchmark with a focus on reproducibility.

**Note:** Hpolib3 is under active construction. Stay tuned for more benchmarks. Information on how to contribute a new benchmark will follow shortly.

## In 4 lines of code

Run a random configuration within a singularity container (requires singularity dependencies: `pip install .[singularity]`)
```python
from hpolib.container.benchmarks.ml.xgboost_benchmark import XGBoostBenchmark
b = XGBoostBenchmark(task_id=167149, container_source='library://phmueller/automl')
config = b.get_configuration_space(seed=1).sample_configuration()
result_dict = b.objective_function_test(config, n_estimators=128, subsample=0.5)
```

Containerized benchmarks do not rely on external dependencies and thus do not change. To do so, we rely on [Singularity (version 3.5)](https://sylabs.io/guides/3.5/user-guide/).
 
Further requirements are: [ConfigSpace](https://github.com/automl/ConfigSpace), *scipy* and *numpy* 

**Note:** Each benchmark can also be run locally, but the dependencies must be installed manually and might conflict with other benchmarks. 
 This can be arbitrarily complex and further information can be found in the docstring of the benchmark.
 
A simple example is the XGBoost benchmark which can be installed with `pip install .[xgboost]`
```python
from hpolib.benchmarks.ml.xgboost_benchmark import XGBoostBenchmark
b = XGBoostBenchmark(task_id=167149)
config = b.get_configuration_space(seed=1).sample_configuration()
result_dict = b.objective_function_test(config, n_estimators=128, subsample=0.5)
```

## Installation

Before we start, we recommend using a virtual environment. To run any benchmark using its singularity container, 
run the following:
```
git clone https://github.com/automl/HPOlib3.git
cd HPOlib3 
pip install .[singularity]
```

**Note:** This does not install *singularity (version 3.5)*. Please follow the steps described here: [user-guide](https://sylabs.io/guides/3.5/user-guide/quick_start.html#quick-installation-steps).   

## Available Containerized Benchmarks

| Benchmark Name                    | Container Name     | Container Source                     | Hosted at | Additional Info                      |
| :-------------------------------- | ------------------ | ------------------------------------ | ----------|-------------------------------------- |
| XGBoostBenchmark                  | xgboost_benchmark  | library://phmueller/automl/xgboost_benchmark | [Sylabs](https://cloud.sylabs.io/library/_container/5f0f610eae86dd3232deb5a5) | Works with OpenML task ids |
| CartpoleFull                      | cartpole           | library://phmueller/automl/cartpole  | [Sylabs](https://cloud.sylabs.io/library/_container/5f0f310084a01836e4395601) | Not deterministic                    |
| CartpoleReduced                   | cartpole           | library://phmueller/automl/cartpole  | [Sylabs](https://cloud.sylabs.io/library/_container/5f0f310084a01836e4395601) | Not deterministic                    |
| Learna                            | learna_benchmark   | library://phmueller/automl/learna_benchmark | [Sylabs](https://cloud.sylabs.io/library/_container/5f0f31c3b1793638c1134e58) | Not deterministic                    |
| MetaLearna                        | learna_benchmark   | library://phmueller/automl/learna_benchmark | [Sylabs](https://cloud.sylabs.io/library/_container/5f0f31c3b1793638c1134e58) | Not deterministic                    |
| SliceLocalizationBenchmark        | tabular_benchmarks | library://phmueller/automl/tabular_benchmarks | [Sylabs](https://cloud.sylabs.io/library/_container/5f0f630cb1793638c1134e5d) | Loading may take several minutes     |
| ProteinStructureBenchmark         | tabular_benchmarks | library://phmueller/automl/tabular_benchmarks | [Sylabs](https://cloud.sylabs.io/library/_container/5f0f630cb1793638c1134e5d) | Loading may take several minutes     |
| NavalPropulsionBenchmark          | tabular_benchmarks | library://phmueller/automl/tabular_benchmarks | [Sylabs](https://cloud.sylabs.io/library/_container/5f0f630cb1793638c1134e5d) | Loading may take several minutes     |
| ParkinsonsTelemonitoringBenchmark | tabular_benchmarks | library://phmueller/automl/tabular_benchmarks | [Sylabs](https://cloud.sylabs.io/library/_container/5f0f630cb1793638c1134e5d) | Loading may take several minutes     |
| NASCifar10ABenchmark              | nasbench_101       | library://phmueller/automl/nasbench_101 | [Sylabs](https://cloud.sylabs.io/library/_container/5f227263b1793638c1135c37) |                                     |
| NASCifar10BBenchmark              | nasbench_101       | library://phmueller/automl/nasbench_101 | [Sylabs](https://cloud.sylabs.io/library/_container/5f227263b1793638c1135c37) |                                     |
| NASCifar10CBenchmark              | nasbench_101       | library://phmueller/automl/nasbench_101 | [Sylabs](https://cloud.sylabs.io/library/_container/5f227263b1793638c1135c37) |                                     |

## Further Notes

### How to build a container locally

With singularity installed run the following to built the xgboost container

```bash
cd hpolib/container/recipes/ml
sudo singularity build xgboost_benchmark Singularity.XGBoostBenchmark
```

You can use this local image with:

```python
from hpolib.container.benchmarks.ml.xgboost_benchmark import XGBoostBenchmark
b = XGBoostBenchmark(task_id=167149, container_name="xgboost_benchmark", 
                     container_source='./') # path to hpolib/container/recipes/ml
config = b.get_configuration_space(seed=1).sample_configuration()
result_dict = b.objective_function_test(config, n_estimators=128, subsample=0.5)
```

### Remove all caches

# HPOlib data
HPOlib stores downloaded containers and datasets at the following locations:

```bash
$XDG_CONFIG_HOME # ~/.config/hpolib3
$XDG_CACHE_HOME # ~/.config/hpolib3
$XDG_DATA_HOME # ~/.cache/hpolib3
```

# OpenML data

OpenML data additionally maintains it's own cache with is found at `~/.openml/`

# Singularity container

Singularity additionally maintains it's own cache which can be removed with `singularity cache clean`

### Troubleshooting

- For users of the Meta-Cluster in Freiburg, you have to set the following path:\
```export PATH=/usr/local/kislurm/singularity-3.5/bin/:$PATH```} \
- Singularity will throw an exception 'Invalid Image format' if you use a singularity version < 3
  
## Status

Status for Master Branch: 

[![Build Status](https://travis-ci.org/automl/HPOlib3.svg?branch=master)](https://travis-ci.org/automl/HPOlib3)
[![codecov](https://codecov.io/gh/automl/HPOlib3/branch/master/graph/badge.svg)](https://codecov.io/gh/automl/HPOlib3)

Status for Development Branch: 

[![Build Status](https://travis-ci.org/automl/HPOlib3.svg?branch=development)](https://travis-ci.org/automl/HPOlib3)
[![codecov](https://codecov.io/gh/automl/HPOlib3/branch/development/graph/badge.svg)](https://codecov.io/gh/automl/HPOlib3)
