# Installation

## Latest version:

`pip install git+https://github.com/xglab-pro/xglab_metric.git`

## Specific version:

`pip install git+https://github.com/xglab-pro/xglab_metric.git@version`

### Example:

`pip install git+https://github.com/xglab-pro/xglab_metric.git@v1.0.0`

The list of version you can find in tag tab

# Add new metric

To create a new metric, inherit from the NumericMetric class and implement the `evaluate` method.

See the [example repository](https://github.com/xglab-pro/xglab_metric_example)