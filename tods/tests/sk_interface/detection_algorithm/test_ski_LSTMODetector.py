# import numpy as np
# import pandas as pd
# import os
# from tods.sk_interface.detection_algorithm.LSTMODetector_skinterface import LSTMODetectorSKI

# from pyod.utils.data import generate_data
# import unittest
# from sklearn.utils.testing import assert_allclose
# from sklearn.utils.testing import assert_array_less
# from sklearn.utils.testing import assert_equal
# from sklearn.utils.testing import assert_greater
# from sklearn.utils.testing import assert_greater_equal
# from sklearn.utils.testing import assert_less_equal
# from sklearn.utils.testing import assert_raises
# from sklearn.metrics import roc_auc_score

# class LSTMODetectorSKI_TestCase(unittest.TestCase):
#     def setUp(self):

#         self.maxDiff = None
#         self.n_train = 200
#         self.n_test = 100
#         self.contamination = 0.1
#         self.roc_floor = 0.0
#         self.X_train, self.y_train, self.X_test, self.y_test = generate_data(
#             n_train=self.n_train, n_test=self.n_test,
#             contamination=self.contamination, random_state=42)

#         #self.y_test = self.y_test[1:]
#         self.y_train = self.y_train[1:]


#         self.transformer = LSTMODetectorSKI(contamination=self.contamination, feature_dim=self.X_train.shape[1])
#         self.transformer.fit(self.X_train)

#     def test_prediction_labels(self):
#         pred_labels = self.transformer.predict(self.X_test)
#         assert_equal(pred_labels.shape[0], self.y_test.shape[0])

#     def test_prediction_score(self):
#         pred_scores = self.transformer.predict_score(self.X_test)
#         assert_equal(pred_scores.shape[0], self.y_test.shape[0])
#         assert_greater_equal(roc_auc_score(self.y_test, pred_scores), self.roc_floor)


# if __name__ == '__main__':
#     unittest.main()
