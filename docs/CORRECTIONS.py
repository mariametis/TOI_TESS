import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt

def get_corr_emp(bprp):
    corr = -0.0051 * bprp - 0.0000 
    return corr

def get_corr_BTSettl_gr55(bprp, Ak):
    # Coefficients from table_BTSettl_g5.5_cut10.tex (deg 5, α=1.0e-04)
    corr2 = (
        -1.329229e-02
        + 1.593053e-02 * bprp
        - 8.733715e-02 * Ak
        - 8.831643e-03 * bprp**2
        + 5.664925e-02 * bprp * Ak
        - 2.357119e-01 * Ak**2
        + 7.858785e-04 * bprp**3
        - 7.628333e-03 * bprp**2 * Ak
        + 1.097561e-01 * bprp * Ak**2
        - 3.082084e-01 * Ak**3
        + 6.854960e-05 * bprp**4
        - 1.491960e-03 * bprp**3 * Ak
        - 4.557967e-03 * bprp**2 * Ak**2
        + 5.332775e-02 * bprp * Ak**3
        - 8.391995e-02 * Ak**4
        - 9.747066e-06 * bprp**5
        + 2.596816e-04 * bprp**4 * Ak
        - 2.134561e-03 * bprp**3 * Ak**2
        + 1.324176e-02 * bprp**2 * Ak**3
        - 5.588693e-02 * bprp * Ak**4
        + 9.991291e-02 * Ak**5
    )
    return corr2


def get_corr_BTSettl_gr40(bprp, Ak):
    # Coefficients from table_BTSettl_g4.0_cut10.tex (deg 5, α=3.2e-06)
    corr2 = (
        -1.273776e-03
        - 5.170282e-03 * bprp
        + 1.178658e-02 * Ak
        + 6.923352e-03 * bprp**2
        - 1.196423e-01 * bprp * Ak
        + 3.517845e-01 * Ak**2
        - 4.563327e-03 * bprp**3
        + 8.948878e-02 * bprp**2 * Ak
        - 5.067602e-01 * bprp * Ak**2
        + 8.823707e-01 * Ak**3
        + 7.845578e-04 * bprp**4
        - 1.991052e-02 * bprp**3 * Ak
        + 1.744724e-01 * bprp**2 * Ak**2
        - 6.929069e-01 * bprp * Ak**3
        + 1.114802e+00 * Ak**4
        - 4.158055e-05 * bprp**5
        + 1.318290e-03 * bprp**4 * Ak
        - 1.584652e-02 * bprp**3 * Ak**2
        + 9.705284e-02 * bprp**2 * Ak**3
        - 2.964960e-01 * bprp * Ak**4
        + 3.369162e-01 * Ak**5
    )
    return corr2
    
def get_corr_BTSettl_gr40_2(bprp, Ak):
    # Coefficients from table_BTSettl_g4.0_cut10.tex (deg 5, α=3.2e-06)
    corr2 = (
        + 2.808332e-05
        - 3.674620e-03 * bprp
        - 6.969206e-03 * Ak
        - 1.854357e-04 * bprp**2
        - 1.325329e-02 * bprp * Ak
        + 2.590481e-02 * Ak**2
        - 5.892869e-04 * bprp**3
        + 5.838539e-03 * bprp**2 * Ak
        - 3.589737e-02 * bprp * Ak**2
        + 1.091646e-01 * Ak**3
        + 1.385153e-04 * bprp**4
        + 3.779117e-05 * bprp**3 * Ak
        - 4.340996e-03 * bprp**2 * Ak**2
        - 3.268350e-02 * bprp * Ak**3
        + 1.592007e-01 * Ak**4
        - 1.869873e-05 * bprp**5
        + 1.676533e-05 * bprp**4 * Ak
        + 9.746702e-04 * bprp**3 * Ak**2
        + 6.702336e-03 * bprp**2 * Ak**3
        - 7.673233e-02 * bprp * Ak**4
        + 1.657967e-01 * Ak**5
    )
    return corr2

def get_corr_Next_gr15(bprp, Ak):
    # Coefficients from table_NextGen_g1.5_cut10.tex (deg 5, α=1.0e-03)
    corrNext15 = (
        + 2.371456e-04
        - 4.469043e-03 * bprp
        + 3.329082e-03 * Ak
        - 8.995278e-04 * bprp**2
        - 1.913143e-02 * bprp * Ak
        + 3.569046e-02 * Ak**2
        + 2.290123e-04 * bprp**3
        + 5.755135e-03 * bprp**2 * Ak
        - 5.492851e-02 * bprp * Ak**2
        + 1.720371e-01 * Ak**3
        - 7.509053e-05 * bprp**4
        + 8.068993e-04 * bprp**3 * Ak
        - 2.746039e-03 * bprp**2 * Ak**2
        - 2.995125e-02 * bprp * Ak**3
        + 1.065885e-01 * Ak**4
        - 1.075279e-05 * bprp**5
        + 1.165779e-04 * bprp**4 * Ak
        + 2.838964e-04 * bprp**3 * Ak**2
        - 2.381658e-03 * bprp**2 * Ak**3
        - 1.750769e-02 * bprp * Ak**4
        + 9.891859e-02 * Ak**5
    )
    return corrNext15


def get_corr_Next_gr55(bprp, Ak):
    # Coefficients from table_NextGen_g5.5_cut10.tex (deg 3, α=3.2e-02)
    corrNext55 = (
        + 4.643040e-03
        - 7.074736e-03 * bprp
        - 5.303975e-04 * Ak
        - 4.064623e-04 * bprp**2
        - 3.616156e-03 * bprp * Ak
        - 3.530954e-02 * Ak**2
        + 3.214983e-05 * bprp**3
        + 3.610048e-05 * bprp**2 * Ak
        + 4.036175e-05 * bprp * Ak**2
        + 9.739784e-03 * Ak**3
    )
    return corrNext55


# ── Input / Output Files ───────────────────────────────────────────────────────

input_file = "tois_synth.correcred.distr.csv"
output_file_distr=input_file+".out_alpha.csv"

data2 = pd.read_csv(input_file)
SyntTESS_cut = data2['SyntTESS_cut']
bprp         = data2['dr3BPRP']
Ebv          = data2['ebv']
#Av =3.1*Ebv
#Ak = Av*0.077  # Set to 0.0 as in your v2 script
ak_raw = 3.1 * Ebv * 0.077
Ak     = np.where(np.isnan(ak_raw), 0.0, ak_raw)      # missing E(B-V): assume A_K = 0 and flag it
intr   = bprp - 4.86 * Ak                              # reddening-corrected colour

# 1. Empirical Correction
corrEmp = get_corr_emp(bprp)+ 0.0031
# 2. Theoretical Correction
corrBTSettl40 = get_corr_BTSettl_gr40_2(bprp, Ak)+ 0.0031
corrBTSettl55 = get_corr_BTSettl_gr55(bprp, Ak)+ 0.0031
corrNext15 = get_corr_Next_gr15(bprp, Ak)+ 0.0031
corrNext55 = get_corr_Next_gr55(bprp, Ak)+ 0.0031


# colour validity ranges (BP-RP, mag)
COLOR_RANGES = {
    'corrEmp': (-1.0,10.0),    
    'BTSettl40': (-0.5,   10.0),
    'BTSettl55': ( 1.15, 10.0),
    'Next55':    ( 1.15, 10.0),
    'Next15':    (-0.332, 10.0),
}

#boundary
BAD = 99.99
def apply_color_limits(corr, bprp, key):
    lo, hi = COLOR_RANGES[key]
    inside = (bprp >= lo) & (bprp <= hi)      # NaN -> False -> flagged
    return corr.where(inside, BAD)

data2['corrEmp'] = apply_color_limits(corrEmp, bprp,'corrEmp')
data2['corrNext15'] =apply_color_limits(corrNext15, bprp,'Next15')
data2['corrNext55'] =apply_color_limits(corrNext55, bprp,'Next55')
data2['corrBTSettl40'] =apply_color_limits(corrBTSettl40, bprp,'BTSettl40')
data2['corrBTSettl55'] =apply_color_limits(corrBTSettl55, bprp,'BTSettl55')


valid40 = (bprp >= -0.5) & (bprp <= 5.0) & (intr >= -0.5)
valid55 = (intr >= 1.15) & (bprp <= 10.0) & (Ak <= 1.4)
c40 = np.where(valid40, corrBTSettl40, np.nan)
c55 = np.where(valid55, corrBTSettl55, np.nan)
mean4055  = np.nanmean(np.vstack([c40, c55]), axis=0)
corrFinal = np.where(bprp < 1.9, c40, mean4055)
corrFinal = np.where(np.isnan(corrFinal), corrEmp, corrFinal)   # fallback, flag these stars
data2['corrFinal']=corrFinal

#corr_cols = [ 'corrBTSettl40', 'corrBTSettl55']
#vals = data2[corr_cols].astype(float)
#vals = vals.mask(vals > 99)
#data2['corrBTSettl40-55'] = vals.mean(axis=1)           # NaN-aware, per star
#data2['corrStd']  = vals.std(axis=1, ddof=1)    # sample sigma across the valid corrections
#data2['corrN']    = vals.count(axis=1)          # how many corrections went into it
#data2['corrFinal'] = np.where(
#   bprp < 1.9,
#   data2['corrBTSettl40'],      # or the logg=4.0 relation
#   data2['corrBTSettl40-55']
#)   
#data2['corrEmp']= np.minimum(data2['corrEmp'], 0.0)
#data2['corrNext15']= np.minimum(data2['corrNext15'], 0.0)
#data2['corrBTSettl40-55']=np.minimum(data2['corrFinal'], 0.0)





# ── Print Verification (First row only, to keep console clean) ───────────────
print("✅ Calculations complete.")
print("\nComparison of first star:")
print(f"  SyntTESS_cut      : {SyntTESS_cut.iloc[0]:.6f}")
print(f"  corr (Emp)        : {corrEmp.iloc[0]:.6f}")
print(f"  corr (Next 1.5)   : {corrNext15.iloc[0]:.6f}")
print(f"  corr (Next 5.5)   : {corrNext55.iloc[0]:.6f}")
print(f"  corr (BTsettl 4.0): {corrBTSettl40.iloc[0]:.6f}")
print(f"  corr (BTsettl 5.5): {corrBTSettl55.iloc[0]:.6f}")
print(f"  Difference        : {corrNext15.iloc[0] - corrBTSettl55.iloc[0]:.6f}")

data3=data2[['dr3_source_id','ebv','dr3BPRP','SyntTESS_cut','SyntTESS_cuterr','corrNext15','corrFinal']]
data3.to_csv(output_file_distr,index=False)

# ==============================================================================
# PLOTTING THE IMPACT
# ==============================================================================
fig, (ax1) = plt.subplots(1, 1, figsize=(10, 10))
# Plot 1: Stellar Radius Change vs Magnitude Difference
ax1.scatter( bprp,data2['corrBTSettl40'], color='red', s=50, edgecolor='black')
ax1.scatter( bprp,data2['corrBTSettl55'], color='pink', s=50, edgecolor='black')
ax1.scatter( bprp,data2['corrNext55'], color='green', s=50, edgecolor='black')
ax1.scatter( bprp,data2['corrNext15'], color='cyan', s=50, edgecolor='black')
ax1.scatter( bprp,data2['corrEmp'], color='yellow', s=50, edgecolor='black')
ax1.scatter( bprp,data2['corrFinal'], color='magenta', s=50, edgecolor='black')
ax1.axhline(0, color='red', linestyle='--', alpha=0.7)
ax1.set_xlabel(r'BP-RP [mag]')
ax1.set_ylabel('Corr  [mag]')
ax1.grid(True, alpha=0.3)
ax1.set_ylim(-0.15, 0.025)


plt.tight_layout()
plt.savefig('test_corr_alpha.png', dpi=300)
