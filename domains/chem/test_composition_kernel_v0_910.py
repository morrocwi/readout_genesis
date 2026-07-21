import unittest
from composition_kernel_v0_910 import *
class TestCompositionKernel(unittest.TestCase):
    def test_carrier(self):
        r=carrier_axiom_receipt(('u','v'),((0,0),(1,0),(0,2),(3,1)))
        self.assertTrue(all(r.values()))
    def test_homomorphism(self):
        r=count_homomorphism_receipt(('u','v'),('u',),('v','u'))
        self.assertTrue(r['empty_to_zero']); self.assertTrue(r['concatenation_to_addition'])
    def test_unknown_obstructed(self):
        with self.assertRaises(ValueError): occupation(('x',),('u','v'))
    def test_alias_obstructed(self):
        self.assertTrue(alias_countermodel()['duplicate_alias_rejected'])
    def test_permutation_positive(self):
        states=('a','b'); words={'a':('u','v'),'b':('v','u')}; profiles={'p':{'readout':{'a':1,'b':1},'successor':{'a':'z','b':'z'}}}
        self.assertEqual(permutation_sufficiency_gate(states,words,('u','v'),profiles)['decision'],'ADMITTED_FOR_REGISTERED_PROFILES')
    def test_permutation_negative(self):
        states=('a','b'); words={'a':('u','v'),'b':('v','u')}; profiles={'p':{'readout':{'a':1,'b':2},'successor':{'a':'z','b':'z'}}}
        self.assertEqual(permutation_sufficiency_gate(states,words,('u','v'),profiles)['decision'],'OBSTRUCTED_COMMUTATIVE_QUOTIENT')
    def test_refinement(self):
        self.assertTrue(refinement_commutation_receipt(((1,1,0),(0,0,1)),(1,2,3),(2,0,1))['commutes'])
        self.assertTrue(invalid_refinement_countercontrol()['all_bad_maps_rejected'])
    def test_lineage(self):
        self.assertTrue(all(lineage_receipt(('u','v','w')).values()))
    def test_suite(self):
        self.assertEqual(run_composition_suite()['decision'],'PASS')
if __name__=='__main__':unittest.main()
