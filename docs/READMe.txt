papero.pdf paper to be submitted

----------------------------------------------------------------------

CORRECTIONS.py  --- Python script which includes all subroutines
                    performing the calculation of the correction for the missing tail

----------------------------------------------------------------------

GaiaXpy.xml     --- file created for the TESSv2cut filter to be used with 
                    GaiaXpy

For your python script, how to call GaiaXpy
from gaiaxpy import PhotometricSystem, load_additional_systems
from gaiaxpy import generate
...
...
# ── Photometric systems ───────────────────────────────────────────────────────
PhotometricSystem.get_available_systems()
PhotometricSystem = load_additional_systems('....../tess_filter')
phot_systems_list = [PhotometricSystem.Gaia_DR3_Vega,PhotometricSystem.USER_TESS]
...
...
# Column names of the synthetic magnitudes as returned by gaiaxpy.generate().
# Inspect one output once if unsure: print(synthetic_photometry.columns.tolist())
COL_G    = 'GaiaDr3Vega_mag_G'
COL_BP   = 'GaiaDr3Vega_mag_BP'
COL_RP   = 'GaiaDr3Vega_mag_RP'
COL_TESS    = 'USER_TESS_mag_Red_v2'   # adjust if your filter file uses a different band name
COL_TESS_cut = 'USER_TESS_mag_Red_v2_crop20'   # adjust if your filter file uses a different band name
...
...
...
synthetic_photometry = generate(f, photometric_system=phot_systems_list,save_file=False)


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

