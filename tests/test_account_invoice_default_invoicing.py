#!/usr/bin/env python
# This file is part of the account_invoice_default_invoicing module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.tests.test_tryton import test_depends, test_view
import os
import sys
import trytond.tests.test_tryton
import unittest
DIR = os.path.abspath(os.path.normpath(os.path.join(__file__,
    '..', '..', '..', '..', '..', 'trytond')))
if os.path.isdir(DIR):
    sys.path.insert(0, os.path.dirname(DIR))


class AccountInvoiceDefaultInvoicingTestCase(unittest.TestCase):
    '''
    Test Account Invoice Default Invoicing module.
    '''

    def setUp(self):
        trytond.tests.test_tryton.install_module('account_invoice_default_invoicing')

    def test0005views(self):
        '''
        Test views.
        '''
        test_view('account_invoice_default_invoicing')

    def test0006depends(self):
        '''
        Test depends.
        '''
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        AccountInvoiceDefaultInvoicingTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
