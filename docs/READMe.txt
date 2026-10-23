papero.pdf paper to be submitted

----------------------------------------------------------------------

CORRECTIONS.py  --- Python script which includes all subroutines
                    performing the calculation of the correction for the missing tail

----------------------------------------------------------------------

GaiaXpy.xml     --- file created for the TESSv2cut filter to be used with 
                    GaiaXpy

----------------------------------------------------------------------
TOI_TESSmag.csv

The csv file contains all stars from the TOI catalog with 
a Gaia DR3 BPRP match (7626 entries). The csv table includes
the following columns:

1-dr3_source_id    ---   Gaia DR3 source_id
2-ebv              ---   reddening as tabulated in the TOI catalog
3-dr3BPRP          ---   Observed Gaia DR3 BP-RP color
4-SyntTESS_cut     ---   Synthetic TESSv2_cut magnitude from Gaia DR3 BP-RP color
5-SyntTESS_cuterr  ---   Error from GaiaXpy on the synthetic TESSv2_cut magnitude
6-corrNext15       ---   Correction for the missing tail using NEXTGen gr1.5 models
7-corrFinal        ---   Correction for the missing tail using BT_SEttl gr4 and gr5.5 models

