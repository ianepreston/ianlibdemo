from ianlibdemo import fun_pandas
from pandas.testing import assert_frame_equal

def test_pandas_integration():
    """Just a test to make sure pandas installs with our package"""
    df1 = fun_pandas.give_me_a_df()
    df2 = fun_pandas.give_me_a_df()
    assert_frame_equal(df1, df2)