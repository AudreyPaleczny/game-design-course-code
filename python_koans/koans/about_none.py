#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutNil in the Ruby Koans
#





# I FINISHED FILLING IN MOST OF THE BLANKS BUT I'M NOT SURE HOW TO CHECK 
# WHETHER IT IS CORRECT --> I CANNOT FILL IN THE BLANKS NEAR THE END THAT
# REQUIRE ME TO RUN IT AND RECEIVE AN ERROR MESSAGE






from runner.koan import *

class AboutNone(Koan):

    def test_none_is_an_object(self):
        "Unlike NULL in a lot of languages"
        self.assertEqual(True, isinstance(None, object))

    def test_none_is_universal(self):
        "There is only one None"
        self.assertEqual(True, None is None) #is this correct?

    def test_what_exception_do_you_get_when_calling_nonexistent_methods(self):
        """
        What is the Exception that is thrown when you call a method that does
        not exist?

        Hint: launch python command console and try the code in the block below.

        Don't worry about what 'try' and 'except' do, we'll talk about this later
        """
        #below reminds me of a try catch in java
        try:
            None.some_method_none_does_not_know_about()
        except Exception as ex:
            ex2 = ex

        # What exception has been caught?
        #
        # Need a recap on how to evaluate __class__ attributes?
        #
        #     https://github.com/gregmalcolm/python_koans/wiki/Class-Attribute

        self.assertEqual(__, ex2.__class__) 


        # I CANNOT RUN THIS SO I CANNOT FILL IN THE BLANK ABOVE AND BELOW


        # What message was attached to the exception?
        # (HINT: replace __ with part of the error message.)
        self.assertRegex(ex2.args[0], __)

    def test_none_is_distinct(self):
        """
        None is distinct from other things which are False.
        """
        self.assertEqual(None, None is not 0)
        self.assertEqual(None, None is not False) #are both these blanks correct as None?
