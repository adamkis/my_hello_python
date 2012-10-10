from nose.tools import assert_equal


from pipes.lib.pipeline import Pipeline

import datetime


class TestClass:
   def test_run_pipeline_1(self):

      input_initial = {
         'original': 'abc'
      }

      input = input_initial

      pipeline = Pipeline()
      pipeline.run(input)
      
      assert_equal( input['original'], 'abc' )
      assert_equal( input['UCASE'], 'ABC' )
      assert_equal( input['DUPLICATED'], 'abc abc' + " " + datetime.datetime.now().strftime("%Y-%m-%d") )

   def test_run_pipeline_2(self):

      input_initial = {
         'original': 'bbb'
      }

      input = input_initial

      pipeline = Pipeline()
      pipeline.run(input)
      
      assert_equal( input['original'], 'bbb' )
      assert_equal( input['UCASE'], 'BBB' )
      assert_equal( input['DUPLICATED'], 'bbb bbb' + " " + datetime.datetime.now().strftime("%Y-%m-%d") )

   def test_run_pipeline_3(self):

      input_initial = {
         'original': '+=%'
      }

      input = input_initial

      pipeline = Pipeline()
      pipeline.run(input)
      
      assert_equal( input['original'], '+=%' )
      assert_equal( input['UCASE'], '+=%' )
      assert_equal( input['DUPLICATED'], '+=% +=%' + " " + datetime.datetime.now().strftime("%Y-%m-%d") )

   def test_run_pipeline_4(self):

      input_initial = {
         'original': '$$$$##&&asdf)()()('
      }

      input = input_initial

      pipeline = Pipeline()
      pipeline.run(input)
      
      assert_equal( input['original'], '$$$$##&&asdf)()()(' )
      assert_equal( input['UCASE'], '$$$$##&&ASDF)()()(' )
      assert_equal( input['DUPLICATED'], '$$$$##&&asdf)()()( $$$$##&&asdf)()()(' + " " + datetime.datetime.now().strftime("%Y-%m-%d") )     

