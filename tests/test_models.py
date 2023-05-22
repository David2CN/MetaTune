from baseline.mixin import SampleClassMixin
import tune_classifier
import tune_regressor
from tests.utils import BaseTest


# run python -m pytest -v


# classification tests
class TestSVC(BaseTest):
    model: SampleClassMixin = tune_classifier.SVCModel
    task: str = "classification"


class TestDecisionTreeClassifier(BaseTest):
    model: SampleClassMixin = tune_classifier.DecisionTreeClassifierModel
    task: str = "classification"


class TestLogisticRegressor(BaseTest):
    model: SampleClassMixin = tune_classifier.LogisticRegressionModel
    task: str = "classification"


class TestLinearSVC(BaseTest):
    model: SampleClassMixin = tune_classifier.LinearSVCModel
    task: str = "classification"


class TestExtraTreeClassifier(BaseTest):
    model: SampleClassMixin = tune_classifier.ExtraTreeClassifierModel
    task: str = "classification"


# regression tests
class TestSVR(BaseTest):
    model: SampleClassMixin = tune_regressor.SVRModel
    task: str = "regression"


class TestDecisionTreeRegressor(BaseTest):
    model: SampleClassMixin = tune_regressor.DecisionTreeRegressorModel
    task: str = "regression"


class TestLinearRegressor(BaseTest):
    model: SampleClassMixin = tune_regressor.LinearRegressionModel
    task: str = "regression"


class TestLassoRegressor(BaseTest):
    model: SampleClassMixin = tune_regressor.LassoModel
    task: str = "regression"


class TestRidgeRegressor(BaseTest):
    model: SampleClassMixin = tune_regressor.RidgeModel
    task: str = "regression"


class TestLinearSVR(BaseTest):
    model: SampleClassMixin = tune_regressor.LinearSVRModel
    task: str = "regression"


class TestExtraTreeRegressor(BaseTest):
    model: SampleClassMixin = tune_regressor.ExtraTreeRegressorModel
    task: str = "regression"


