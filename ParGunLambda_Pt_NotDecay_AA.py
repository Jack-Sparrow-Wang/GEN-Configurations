import FWCore.ParameterSet.Config as cms

generator = cms.EDFilter("Pythia8PtGun",
        PGunParameters = cms.PSet(
        MaxPt = cms.double(6.05),
        MinPt = cms.double(0.75),
        ParticleID = cms.vint32(3122, 3122, 3122, 3122, 3122,-3122, -3122, -3122, -3122, -3122,3122, 3122, 3122, 3122, 3122,-3122, -3122, -3122, -3122, -3122,3122, 3122, 3122, 3122, 3122,-3122, -3122, -3122, -3122, -3122,3122, 3122, 3122, 3122, 3122,-3122, -3122, -3122, -3122, -3122),
        AddAntiParticle = cms.bool(False),
        MaxEta = cms.double(2.55), #eta 2.55 
        MaxPhi = cms.double(3.14159265359),
        MinEta = cms.double(-2.55), #eta -2.55 
        MinPhi = cms.double(-3.14159265359) ## in radians
    ),
    Verbosity = cms.untracked.int32(0), ## set to 1 (or greater)  for printouts
    psethack = cms.string('lambda Pt 0.75 to 6.05'),
    firstRun = cms.untracked.uint32(1),
    #PythiaParameters = cms.PSet(parameterSets = cms.vstring())

    PythiaParameters = cms.PSet(
	py8LambdaDecaySettings = cms.vstring('3122:onMode = off' # turn OFF all Lambda decays
	),
        parameterSets = cms.vstring(  
	                              'py8LambdaDecaySettings' 
				   )
    )

)
