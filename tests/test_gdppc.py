import impactcommon

provider_low = GDPpcProvider('low', 'SSP3')
provider_high = GDPpcProvider('high', 'SSP3')

# ZWE exists in both IAMs: check that correct and different

def test_zwe_low():
    helper(provider_low, 'ZWE.2.2', 188.74704269, 569.97540343, 576.72664619)

def test_zwe_high():
    helper(provider_high, 'ZWE.2.2', 607.12035717, 1846.70740714, 1929.81909533)

# ABW exists only in the high IAM: check that the same
    
def test_abw_low():
    helper(provider_low, 'ABW', 1411.21495327, 4268.54105942, 4391.36859299)

def test_abw_high():
    helper(provider_high, 'ABW', 1411.21495327, 4268.54105942, 4391.36859299)

# XYZ is not a country; check that starts same and grows differently
    
def test_xyz_low():
    helper(provider_low, 'XYZ.1.2', 7065.37128841, 12746.22361976, 12873.57291254)

def test_xyz_high():
    helper(provider_high, 'XYZ.1.2', 7065.37128841, 14553.73370414, 14770.53335484)
    
def helper(provider, region, in2010, in2050, in2051):
    assert provider.get_startyear() <= 2010
    series = provider.get_timeseries(region)
    assert series[2010 - provider.get_startyear()] == in2010
    assert series[2050 - provider.get_startyear()] == in2050
    assert series[2051 - provider.get_startyear()] == in2051

    

