# include <exception>
# include <iostream>
# include <random>
# include <stdlib.h>
# include <string.h>
# include <time.h>
# include <typeinfo>
# include <vector>

# include <boost/program_options.hpp>

# include <TCanvas.h>
# include <TClonesArray.h>
# include <TFile.h>
# include <TH1F.h>
# include <TH2F.h>
# include <TLorentzVector.h>
# include <TMath.h>
# include <TMatrixD.h>
# include <TROOT.h>
# include <TStyle.h>
# include <TSystem.h>
# include <TVectorD.h>

# include <CLHEP/Vector/LorentzVector.h>

# include "fastjet/PseudoJet.hh"
# include "fastjet/ClusterSequence.hh"

# include "fastjet/contrib/AxesDefinition.hh"
# include "fastjet/contrib/EnergyCorrelator.hh"
# include "fastjet/contrib/MeasureDefinition.hh"
# include "fastjet/contrib/Nsubjettiness.hh"
# include "fastjet/contrib/SoftDrop.hh"

# include "AnalysisParameters.h"
# include "BackgroundModel.h"
# include "Deconstruct.h"
# include "Exception.h"
# include "ISRModel.h"
# include "TopGluonModel.h"

# include "HEPTopTagger.hh"

# include "classes/DelphesClasses.h"
# include "external/ExRootAnalysis/ExRootTreeReader.h"
# include "external/ExRootAnalysis/ExRootResult.h"

# include "HeaderFiles/lester_mt2_bisect_mod.h"


std::random_device _randomDevice;  //Will be used to obtain a seed for the random number engine
std::mt19937 _randomEngine(_randomDevice()); //Standard mersenne_twister_engine seeded with rd()


int _defaultVal = -99;

int _defaultVal1 = 99;

double _glu_pTcut = 30;
double _glu_etaCut = 2.4;

double _c_pTcut = 5;
double _c_etaCut = 2.4;

double _b_pTcut = 5;
double _b_etaCut = 2.4;

double _t_pTcut = 50;
double _t_etaCut = 2.4;

double _el_pTcut = 30;
double _el_etaCut = 2.4;
double _el_relIsoCut = 0.15;

double _mu_pTcut = 30;
double _mu_etaCut = 2.4;
double _mu_relIsoCut = 0.15;

double _jet_pTcut = 20;
double _jet_etaCut = 2.4;

double _jetR = 0.4;
//double _fatJetR = 1.0;
double _fatJetR = 1.5;
double _fatJetRby2 = _fatJetR / 2.0;
double _microJetR = 0.2;

int _hepTop_tauN_max = 4;
int _hepTop_CN_max = 3;

double _t_m = 173;
double _W_m = 80.379;
double _WbyTop_mRatio = _W_m / _t_m;

double _jetRescale_m0 = 1.0;
double _jetLorentzBoost_E0 = 2.0;
double _jetLorentzBoost_P0 = std::sqrt(_jetLorentzBoost_E0*_jetLorentzBoost_E0 - _jetRescale_m0*_jetRescale_m0);

double _topRF_jetRescale_m0 = 1.0;
double _topRF_jetLorentzBoost_E0 = 1.001;
double _topRF_jetLorentzBoost_P0 = std::sqrt(_topRF_jetLorentzBoost_E0*_topRF_jetLorentzBoost_E0 - _topRF_jetRescale_m0*_topRF_jetRescale_m0);

int _image_nBinX = 50;
int _image_nBinY = 50;


enum class _DELPHES_RECOID
{
    _DELPHES_RECOID_CONST = 10000,
    
    _DELPHES_RECOID_TRACK = 0,
    _DELPHES_RECOID_PHOTON = 1,
    _DELPHES_RECOID_NEUTRALHADRON = 2,
};

std::string _showerDecon_inputCard = "showerDecon_inputCard.dat";


class OutputInfo
{
    public:
    
    TTree *tree;
    
    
    // Hadronic top
    int hadTop_n_truth;
    std::vector <double> v_hadTop_pT_truth;
    std::vector <double> v_hadTop_eta_truth;
    std::vector <double> v_hadTop_phi_truth;
    std::vector <double> v_hadTop_m_truth;
    std::vector <double> v_hadTop_E_truth;
    std::vector <double> v_hadTop_px_truth;
    std::vector <double> v_hadTop_py_truth;
    std::vector <double> v_hadTop_pz_truth;
    
    
    // b from hadronic top
    int hadTopB_n_truth;
    std::vector <double> v_hadTopB_pT_truth;
    std::vector <double> v_hadTopB_eta_truth;
    std::vector <double> v_hadTopB_phi_truth;
    std::vector <double> v_hadTopB_E_truth;
    std::vector <double> v_hadTopB_px_truth;
    std::vector <double> v_hadTopB_py_truth;
    std::vector <double> v_hadTopB_pz_truth;
    std::vector <double> v_hadTopB_Wq1deltaR_truth;
    std::vector <double> v_hadTopB_Wq2deltaR_truth;
    std::vector <double> v_hadTopB_hadTopDeltaR_truth;
    
    
    // W from hadronic top
    int hadTopW_n_truth;
    std::vector <double> v_hadTopW_pT_truth;
    std::vector <double> v_hadTopW_eta_truth;
    std::vector <double> v_hadTopW_phi_truth;
    std::vector <double> v_hadTopW_E_truth;
    std::vector <double> v_hadTopW_px_truth;
    std::vector <double> v_hadTopW_py_truth;
    std::vector <double> v_hadTopW_pz_truth;
    
    
    // Hadronic W q1
    std::vector <double> v_Wq1_pT_truth;
    std::vector <double> v_Wq1_eta_truth;
    std::vector <double> v_Wq1_phi_truth;
    std::vector <double> v_Wq1_E_truth;
    std::vector <double> v_Wq1_px_truth;
    std::vector <double> v_Wq1_py_truth;
    std::vector <double> v_Wq1_pz_truth;
    std::vector <double> v_Wq1_pid_truth;
    std::vector <double> v_Wq1_Wq2deltaR_truth;
    std::vector <double> v_Wq1_hadTopDeltaR_truth;
    
    
    // Hadronic W q2
    std::vector <double> v_Wq2_pT_truth;
    std::vector <double> v_Wq2_eta_truth;
    std::vector <double> v_Wq2_phi_truth;
    std::vector <double> v_Wq2_E_truth;
    std::vector <double> v_Wq2_px_truth;
    std::vector <double> v_Wq2_py_truth;
    std::vector <double> v_Wq2_pz_truth;
    std::vector <double> v_Wq2_pid_truth;
    std::vector <double> v_Wq2_hadTopDeltaR_truth;
    
    
    std::vector <double> v_cosThetaStar_truth;
    std::vector <double> v_zk_truth;
    std::vector <double> v_zb_truth;
    
    
    // Leptonic top
    int lepTop_n_truth;
    std::vector <double> v_lepTop_pT_truth;
    std::vector <double> v_lepTop_eta_truth;
    std::vector <double> v_lepTop_phi_truth;
    std::vector <double> v_lepTop_m_truth;
    std::vector <double> v_lepTop_E_truth;
    std::vector <double> v_lepTop_px_truth;
    std::vector <double> v_lepTop_py_truth;
    std::vector <double> v_lepTop_pz_truth;
    
    std::vector <double> v_lepTopVis_pT_truth;
    std::vector <double> v_lepTopVis_eta_truth;
    std::vector <double> v_lepTopVis_phi_truth;
    std::vector <double> v_lepTopVis_m_truth;
    std::vector <double> v_lepTopVis_E_truth;
    std::vector <double> v_lepTopVis_px_truth;
    std::vector <double> v_lepTopVis_py_truth;
    std::vector <double> v_lepTopVis_pz_truth;
    
    
    // b from leptonic top
    std::vector <double> v_lepTopB_pT_truth;
    std::vector <double> v_lepTopB_eta_truth;
    std::vector <double> v_lepTopB_phi_truth;
    std::vector <double> v_lepTopB_E_truth;
    std::vector <double> v_lepTopB_px_truth;
    std::vector <double> v_lepTopB_py_truth;
    std::vector <double> v_lepTopB_pz_truth;
    std::vector <double> v_lepTopB_lepTopDeltaR_truth;
    std::vector <double> v_lepTopB_lepTopVisDeltaR_truth;
    
    
    // W from leptonic top
    std::vector <double> v_lepTopW_pT_truth;
    std::vector <double> v_lepTopW_eta_truth;
    std::vector <double> v_lepTopW_phi_truth;
    std::vector <double> v_lepTopW_E_truth;
    std::vector <double> v_lepTopW_px_truth;
    std::vector <double> v_lepTopW_py_truth;
    std::vector <double> v_lepTopW_pz_truth;
    
    
    // Leptonic W lepton
    std::vector <double> v_Wlep_pT_truth;
    std::vector <double> v_Wlep_eta_truth;
    std::vector <double> v_Wlep_phi_truth;
    std::vector <double> v_Wlep_E_truth;
    std::vector <double> v_Wlep_px_truth;
    std::vector <double> v_Wlep_py_truth;
    std::vector <double> v_Wlep_pz_truth;
    std::vector <double> v_Wlep_pid_truth;
    std::vector <double> v_Wlep_lepTopDeltaR_truth;
    std::vector <double> v_Wlep_lepTopVisDeltaR_truth;
    
    
    std::vector <double> v_lepTop_deltaRbl_truth;
    std::vector <double> v_lepTop_mbl_truth;
    std::vector <double> v_zl_truth;
    
    
    // c
    int c_n_truth;
    std::vector <double> v_c_pT_truth;
    std::vector <double> v_c_eta_truth;
    std::vector <double> v_c_phi_truth;
    std::vector <double> v_c_E_truth;
    std::vector <double> v_c_px_truth;
    std::vector <double> v_c_py_truth;
    std::vector <double> v_c_pz_truth;
    
    
    // b
    int b_n_truth;
    std::vector <double> v_b_pT_truth;
    std::vector <double> v_b_eta_truth;
    std::vector <double> v_b_phi_truth;
    std::vector <double> v_b_E_truth;
    std::vector <double> v_b_px_truth;
    std::vector <double> v_b_py_truth;
    std::vector <double> v_b_pz_truth;
    
    
    // Reco top
    int hepTop_n_reco;
    
    std::vector <double> v_hepTop_raw_pT_reco;
    std::vector <double> v_hepTop_raw_eta_reco;
    std::vector <double> v_hepTop_raw_phi_reco;
    std::vector <double> v_hepTop_raw_E_reco;
    std::vector <double> v_hepTop_raw_px_reco;
    std::vector <double> v_hepTop_raw_py_reco;
    std::vector <double> v_hepTop_raw_pz_reco;
    std::vector <double> v_hepTop_raw_m_reco;
    
    std::vector <double> v_hepTop_pT_reco;
    std::vector <double> v_hepTop_eta_reco;
    std::vector <double> v_hepTop_phi_reco;
    std::vector <double> v_hepTop_E_reco;
    std::vector <double> v_hepTop_px_reco;
    std::vector <double> v_hepTop_py_reco;
    std::vector <double> v_hepTop_pz_reco;
    std::vector <double> v_hepTop_m_reco;
    
    std::vector <double> v_hepTop_nExcSubJet_reco;
    
    std::vector <double> v_hepTop_subJet12_m_reco;
    std::vector <double> v_hepTop_subJet23_m_reco;
    std::vector <double> v_hepTop_subJet31_m_reco;
    
    std::vector <double> v_hepTop_subJet123_m_reco;
    
    std::vector <double> v_hepTop_frec_reco;
    
    std::vector <double> v_hepTop_nSubJetBtagged_reco;
    std::vector <double> v_hepTop_nSubJetBmatched_reco;
    std::vector <double> v_hepTop_subJet1B_deltaR_reco;
    std::vector <double> v_hepTop_subJet2B_deltaR_reco;
    std::vector <double> v_hepTop_subJet3B_deltaR_reco;
    
    std::vector <double> v_hepTop_nBinFatJet_reco;
    std::vector <double> v_hepTop_nBtaggedJetInFatJet_reco;
    
    std::vector <double> v_hepTop_showerDecon_chi_reco;
    std::vector <double> v_hepTop_showerDecon_logChi_reco;
    
    std::vector <double> v_hepTop_zk_reco;
    std::vector <double> v_hepTop_zb_reco;
    std::vector <double> v_hepTop_cosThetaStar_reco;
    
    std::vector <double> v_hepTop_zl_reco;
    
    std::vector <double> v_hepTop_lep_subJetLep_genLep_deltaR_reco;
    std::vector <double> v_hepTop_lep_subJetLep_genB_deltaR_reco;
    std::vector <double> v_hepTop_lep_subJetB_genB_deltaR_reco;
    std::vector <double> v_hepTop_lep_subJetB_genLep_deltaR_reco;
    
    std::vector <double> v_hepTop_lepSubJet1_miniIso_reco;
    std::vector <double> v_hepTop_lepSubJet2_miniIso_reco;
    
    std::vector <double> v_hepTop_nearestGenHadTop_index;
    std::vector <double> v_hepTop_nearestGenLepTop_index;
    
    std::vector <double> v_hepTop_genHadTop_deltaR_reco;
    std::vector <double> v_hepTop_genLepTop_deltaR_reco;
    
    std::vector <double> v_hepTop_nGenTopConstiMatched_reco;
    
    std::vector <double> v_hepTop_isMayBeTop_reco;
    std::vector <double> v_hepTop_isTagged_reco;
    
    int hepTop_tauN_max;
    std::vector <std::vector <double> > vv_hepTop_tauN_reco;
    std::vector <std::vector <double> > vv_hepTop_tauNratio_reco;
    
    int hepTop_CN_max;
    std::vector <std::vector <double> > vv_hepTop_CN_reco;
    
    //
    std::vector <TH2F> v_h2_hepTop_fracE_phiEtaPlane_reco;
    std::vector <TH2F> v_h2_hepTop_track_fracE_phiEtaPlane_reco;
    std::vector <TH2F> v_h2_hepTop_photon_fracE_phiEtaPlane_reco;
    std::vector <TH2F> v_h2_hepTop_neutralHad_fracE_phiEtaPlane_reco;
    
    std::vector <TH2F> v_h2_hepTop_boosted_fracE_phiEtaPlane_reco;
    std::vector <TH2F> v_h2_hepTop_boosted_track_fracE_phiEtaPlane_reco;
    std::vector <TH2F> v_h2_hepTop_boosted_photon_fracE_phiEtaPlane_reco;
    std::vector <TH2F> v_h2_hepTop_boosted_neutralHad_fracE_phiEtaPlane_reco;
    
    std::vector <TH2F> v_h2_hepTop_boosted_rescaled_fracE_phiEtaPlane_reco;
    std::vector <TH2F> v_h2_hepTop_boosted_rescaled_track_fracE_phiEtaPlane_reco;
    std::vector <TH2F> v_h2_hepTop_boosted_rescaled_photon_fracE_phiEtaPlane_reco;
    std::vector <TH2F> v_h2_hepTop_boosted_rescaled_neutralHad_fracE_phiEtaPlane_reco;
    
    std::vector <TH2F> v_h2_hepTop_topRestFrame_fracE_phiEtaPlane_reco;
    std::vector <TH2F> v_h2_hepTop_topRestFrame_track_fracE_phiEtaPlane_reco;
    std::vector <TH2F> v_h2_hepTop_topRestFrame_photon_fracE_phiEtaPlane_reco;
    std::vector <TH2F> v_h2_hepTop_topRestFrame_neutralHad_fracE_phiEtaPlane_reco;
    
    std::vector <TH2F> v_h2_hepTop_topRestFrame_rescaled_fracE_phiEtaPlane_reco;
    std::vector <TH2F> v_h2_hepTop_topRestFrame_rescaled_track_fracE_phiEtaPlane_reco;
    std::vector <TH2F> v_h2_hepTop_topRestFrame_rescaled_photon_fracE_phiEtaPlane_reco;
    std::vector <TH2F> v_h2_hepTop_topRestFrame_rescaled_neutralHad_fracE_phiEtaPlane_reco;
    
    std::vector <TH2F> v_h2_hepTop_imageBtagged_reco;
    
    
    OutputInfo(int hepTop_tauN_max = 0, int hepTop_CN_max = 0)
    {
        tree = new TTree("tree", "tree");
        
        
        //
        tree->Branch("hadTop_n_truth", &hadTop_n_truth);
        tree->Branch("hadTop_pT_truth", &v_hadTop_pT_truth);
        tree->Branch("hadTop_eta_truth", &v_hadTop_eta_truth);
        tree->Branch("hadTop_phi_truth", &v_hadTop_phi_truth);
        tree->Branch("hadTop_m_truth", &v_hadTop_m_truth);
        tree->Branch("hadTop_E_truth", &v_hadTop_E_truth);
        tree->Branch("hadTop_px_truth", &v_hadTop_px_truth);
        tree->Branch("hadTop_py_truth", &v_hadTop_py_truth);
        tree->Branch("hadTop_pz_truth", &v_hadTop_pz_truth);
        
        
        tree->Branch("hadTopB_n_truth", &hadTopB_n_truth);
        tree->Branch("hadTopB_pT_truth", &v_hadTopB_pT_truth);
        tree->Branch("hadTopB_eta_truth", &v_hadTopB_eta_truth);
        tree->Branch("hadTopB_phi_truth", &v_hadTopB_phi_truth);
        tree->Branch("hadTopB_E_truth", &v_hadTopB_E_truth);
        tree->Branch("hadTopB_px_truth", &v_hadTopB_px_truth);
        tree->Branch("hadTopB_py_truth", &v_hadTopB_py_truth);
        tree->Branch("hadTopB_pz_truth", &v_hadTopB_pz_truth);
        tree->Branch("hadTopB_Wq1deltaR_truth", &v_hadTopB_Wq1deltaR_truth);
        tree->Branch("hadTopB_Wq2deltaR_truth", &v_hadTopB_Wq2deltaR_truth);
        tree->Branch("hadTopB_hadTopDeltaR_truth", &v_hadTopB_hadTopDeltaR_truth);
        
        
        tree->Branch("hadTopW_n_truth", &hadTopW_n_truth);
        tree->Branch("hadTopW_pT_truth", &v_hadTopW_pT_truth);
        tree->Branch("hadTopW_eta_truth", &v_hadTopW_eta_truth);
        tree->Branch("hadTopW_phi_truth", &v_hadTopW_phi_truth);
        tree->Branch("hadTopW_E_truth", &v_hadTopW_E_truth);
        tree->Branch("hadTopW_px_truth", &v_hadTopW_px_truth);
        tree->Branch("hadTopW_py_truth", &v_hadTopW_py_truth);
        tree->Branch("hadTopW_pz_truth", &v_hadTopW_pz_truth);
        
        
        tree->Branch("Wq1_pT_truth", &v_Wq1_pT_truth);
        tree->Branch("Wq1_eta_truth", &v_Wq1_eta_truth);
        tree->Branch("Wq1_phi_truth", &v_Wq1_phi_truth);
        tree->Branch("Wq1_E_truth", &v_Wq1_E_truth);
        tree->Branch("Wq1_px_truth", &v_Wq1_px_truth);
        tree->Branch("Wq1_py_truth", &v_Wq1_py_truth);
        tree->Branch("Wq1_pz_truth", &v_Wq1_pz_truth);
        tree->Branch("Wq1_pid_truth", &v_Wq1_pid_truth);
        tree->Branch("Wq1_Wq2deltaR_truth", &v_Wq1_Wq2deltaR_truth);
        tree->Branch("Wq1_hadTopDeltaR_truth", &v_Wq1_hadTopDeltaR_truth);
        
        
        tree->Branch("Wq2_pT_truth", &v_Wq2_pT_truth);
        tree->Branch("Wq2_eta_truth", &v_Wq2_eta_truth);
        tree->Branch("Wq2_phi_truth", &v_Wq2_phi_truth);
        tree->Branch("Wq2_E_truth", &v_Wq2_E_truth);
        tree->Branch("Wq2_px_truth", &v_Wq2_px_truth);
        tree->Branch("Wq2_py_truth", &v_Wq2_py_truth);
        tree->Branch("Wq2_pz_truth", &v_Wq2_pz_truth);
        tree->Branch("Wq2_pid_truth", &v_Wq2_pid_truth);
        tree->Branch("Wq2_hadTopDeltaR_truth", &v_Wq2_hadTopDeltaR_truth);
        
        
        tree->Branch("cosThetaStar_truth", &v_cosThetaStar_truth);
        tree->Branch("zk_truth", &v_zk_truth);
        tree->Branch("zb_truth", &v_zb_truth);
        
        
        //
        tree->Branch("lepTop_n_truth", &lepTop_n_truth);
        tree->Branch("lepTop_pT_truth", &v_lepTop_pT_truth);
        tree->Branch("lepTop_eta_truth", &v_lepTop_eta_truth);
        tree->Branch("lepTop_phi_truth", &v_lepTop_phi_truth);
        tree->Branch("lepTop_m_truth", &v_lepTop_m_truth);
        tree->Branch("lepTop_E_truth", &v_lepTop_E_truth);
        tree->Branch("lepTop_px_truth", &v_lepTop_px_truth);
        tree->Branch("lepTop_py_truth", &v_lepTop_py_truth);
        tree->Branch("lepTop_pz_truth", &v_lepTop_pz_truth);
        
        tree->Branch("lepTopVis_pT_truth", &v_lepTopVis_pT_truth);
        tree->Branch("lepTopVis_eta_truth", &v_lepTopVis_eta_truth);
        tree->Branch("lepTopVis_phi_truth", &v_lepTopVis_phi_truth);
        tree->Branch("lepTopVis_m_truth", &v_lepTopVis_m_truth);
        tree->Branch("lepTopVis_E_truth", &v_lepTopVis_E_truth);
        tree->Branch("lepTopVis_px_truth", &v_lepTopVis_px_truth);
        tree->Branch("lepTopVis_py_truth", &v_lepTopVis_py_truth);
        tree->Branch("lepTopVis_pz_truth", &v_lepTopVis_pz_truth);
        
        
        tree->Branch("lepTopB_pT_truth", &v_lepTopB_pT_truth);
        tree->Branch("lepTopB_eta_truth", &v_lepTopB_eta_truth);
        tree->Branch("lepTopB_phi_truth", &v_lepTopB_phi_truth);
        tree->Branch("lepTopB_E_truth", &v_lepTopB_E_truth);
        tree->Branch("lepTopB_px_truth", &v_lepTopB_px_truth);
        tree->Branch("lepTopB_py_truth", &v_lepTopB_py_truth);
        tree->Branch("lepTopB_pz_truth", &v_lepTopB_pz_truth);
        tree->Branch("lepTopB_lepTopDeltaR_truth", &v_lepTopB_lepTopDeltaR_truth);
        tree->Branch("lepTopB_lepTopVisDeltaR_truth", &v_lepTopB_lepTopVisDeltaR_truth);
        
        
        tree->Branch("lepTopW_pT_truth", &v_lepTopW_pT_truth);
        tree->Branch("lepTopW_eta_truth", &v_lepTopW_eta_truth);
        tree->Branch("lepTopW_phi_truth", &v_lepTopW_phi_truth);
        tree->Branch("lepTopW_E_truth", &v_lepTopW_E_truth);
        tree->Branch("lepTopW_px_truth", &v_lepTopW_px_truth);
        tree->Branch("lepTopW_py_truth", &v_lepTopW_py_truth);
        tree->Branch("lepTopW_pz_truth", &v_lepTopW_pz_truth);
        
        
        tree->Branch("Wlep_pT_truth", &v_Wlep_pT_truth);
        tree->Branch("Wlep_eta_truth", &v_Wlep_eta_truth);
        tree->Branch("Wlep_phi_truth", &v_Wlep_phi_truth);
        tree->Branch("Wlep_E_truth", &v_Wlep_E_truth);
        tree->Branch("Wlep_px_truth", &v_Wlep_px_truth);
        tree->Branch("Wlep_py_truth", &v_Wlep_py_truth);
        tree->Branch("Wlep_pz_truth", &v_Wlep_pz_truth);
        tree->Branch("Wlep_pid_truth", &v_Wlep_pid_truth);
        tree->Branch("Wlep_lepTopDeltaR_truth", &v_Wlep_lepTopDeltaR_truth);
        tree->Branch("Wlep_lepTopVisDeltaR_truth", &v_Wlep_lepTopVisDeltaR_truth);
        
        tree->Branch("lepTop_deltaRbl_truth", &v_lepTop_deltaRbl_truth);
        tree->Branch("lepTop_mbl_truth", &v_lepTop_mbl_truth);
        tree->Branch("zl_truth", &v_zl_truth);
        
        
        //
        tree->Branch("c_n_truth", &c_n_truth);
        tree->Branch("c_pT_truth", &v_c_pT_truth);
        tree->Branch("c_eta_truth", &v_c_eta_truth);
        tree->Branch("c_phi_truth", &v_c_phi_truth);
        tree->Branch("c_E_truth", &v_c_E_truth);
        tree->Branch("c_px_truth", &v_c_px_truth);
        tree->Branch("c_py_truth", &v_c_py_truth);
        tree->Branch("c_pz_truth", &v_c_pz_truth);
        
        
        tree->Branch("b_n_truth", &b_n_truth);
        tree->Branch("b_pT_truth", &v_b_pT_truth);
        tree->Branch("b_eta_truth", &v_b_eta_truth);
        tree->Branch("b_phi_truth", &v_b_phi_truth);
        tree->Branch("b_E_truth", &v_b_E_truth);
        tree->Branch("b_px_truth", &v_b_px_truth);
        tree->Branch("b_py_truth", &v_b_py_truth);
        tree->Branch("b_pz_truth", &v_b_pz_truth);
        
        
        //
        tree->Branch("hepTop_n_reco", &hepTop_n_reco);
        
        tree->Branch("hepTop_raw_pT_reco", &v_hepTop_raw_pT_reco);
        tree->Branch("hepTop_raw_eta_reco", &v_hepTop_raw_eta_reco);
        tree->Branch("hepTop_raw_phi_reco", &v_hepTop_raw_phi_reco);
        tree->Branch("hepTop_raw_E_reco", &v_hepTop_raw_E_reco);
        tree->Branch("hepTop_raw_px_reco", &v_hepTop_raw_px_reco);
        tree->Branch("hepTop_raw_py_reco", &v_hepTop_raw_py_reco);
        tree->Branch("hepTop_raw_pz_reco", &v_hepTop_raw_pz_reco);
        tree->Branch("hepTop_raw_m_reco", &v_hepTop_raw_m_reco);
        
        tree->Branch("hepTop_pT_reco", &v_hepTop_pT_reco);
        tree->Branch("hepTop_eta_reco", &v_hepTop_eta_reco);
        tree->Branch("hepTop_phi_reco", &v_hepTop_phi_reco);
        tree->Branch("hepTop_E_reco", &v_hepTop_E_reco);
        tree->Branch("hepTop_px_reco", &v_hepTop_px_reco);
        tree->Branch("hepTop_py_reco", &v_hepTop_py_reco);
        tree->Branch("hepTop_pz_reco", &v_hepTop_pz_reco);
        tree->Branch("hepTop_m_reco", &v_hepTop_m_reco);
        
        tree->Branch("hepTop_nExcSubJet_reco", &v_hepTop_nExcSubJet_reco);
        
        tree->Branch("hepTop_subJet12_m_reco", &v_hepTop_subJet12_m_reco);
        tree->Branch("hepTop_subJet23_m_reco", &v_hepTop_subJet23_m_reco);
        tree->Branch("hepTop_subJet31_m_reco", &v_hepTop_subJet31_m_reco);
        
        tree->Branch("hepTop_subJet123_m_reco", &v_hepTop_subJet123_m_reco);
        
        tree->Branch("hepTop_frec_reco", &v_hepTop_frec_reco);
        
        tree->Branch("hepTop_nSubJetBtagged_reco", &v_hepTop_nSubJetBtagged_reco);
        tree->Branch("hepTop_nSubJetBmatched_reco", &v_hepTop_nSubJetBmatched_reco);
        tree->Branch("hepTop_subJet1B_deltaR_reco", &v_hepTop_subJet1B_deltaR_reco);
        tree->Branch("hepTop_subJet2B_deltaR_reco", &v_hepTop_subJet2B_deltaR_reco);
        tree->Branch("hepTop_subJet3B_deltaR_reco", &v_hepTop_subJet3B_deltaR_reco);
        
        tree->Branch("hepTop_nBinFatJet_reco", &v_hepTop_nBinFatJet_reco);
        tree->Branch("hepTop_nBtaggedJetInFatJet_reco", &v_hepTop_nBtaggedJetInFatJet_reco);
        
        tree->Branch("hepTop_showerDecon_chi_reco", &v_hepTop_showerDecon_chi_reco);
        tree->Branch("hepTop_showerDecon_logChi_reco", &v_hepTop_showerDecon_logChi_reco);
        
        tree->Branch("hepTop_zk_reco", &v_hepTop_zk_reco);
        tree->Branch("hepTop_zb_reco", &v_hepTop_zb_reco);
        tree->Branch("hepTop_cosThetaStar_reco", &v_hepTop_cosThetaStar_reco);
        
        tree->Branch("hepTop_zl_reco", &v_hepTop_zl_reco);
        
        tree->Branch("hepTop_lep_subJetLep_genLep_deltaR_reco", &v_hepTop_lep_subJetLep_genLep_deltaR_reco);
        tree->Branch("hepTop_lep_subJetLep_genB_deltaR_reco", &v_hepTop_lep_subJetLep_genB_deltaR_reco);
        tree->Branch("hepTop_lep_subJetB_genB_deltaR_reco", &v_hepTop_lep_subJetB_genB_deltaR_reco);
        tree->Branch("hepTop_lep_subJetB_genLep_deltaR_reco", &v_hepTop_lep_subJetB_genLep_deltaR_reco);
        
        tree->Branch("hepTop_lepSubJet1_miniIso_reco", &v_hepTop_lepSubJet1_miniIso_reco);
        tree->Branch("hepTop_lepSubJet2_miniIso_reco", &v_hepTop_lepSubJet2_miniIso_reco);
        
        tree->Branch("hepTop_nearestGenHadTop_index", &v_hepTop_nearestGenHadTop_index);
        tree->Branch("hepTop_nearestGenLepTop_index", &v_hepTop_nearestGenLepTop_index);
        
        tree->Branch("hepTop_genHadTop_deltaR_reco", &v_hepTop_genHadTop_deltaR_reco);
        tree->Branch("hepTop_genLepTop_deltaR_reco", &v_hepTop_genLepTop_deltaR_reco);
        
        tree->Branch("hepTop_nGenTopConstiMatched_reco", &v_hepTop_nGenTopConstiMatched_reco);
        
        tree->Branch("hepTop_isMayBeTop_reco", &v_hepTop_isMayBeTop_reco);
        tree->Branch("hepTop_isTagged_reco", &v_hepTop_isTagged_reco);
        
        
        this->hepTop_tauN_max = hepTop_tauN_max;
        
        vv_hepTop_tauN_reco.resize(hepTop_tauN_max+1, {});
        vv_hepTop_tauNratio_reco.resize(hepTop_tauN_max+1, {});
        
        for(int iTauN = 0; iTauN <= hepTop_tauN_max; iTauN++)
        {
            char brName[1000];
            
            sprintf(brName, "hepTop_tau%d_reco", iTauN);
            tree->Branch(brName, &vv_hepTop_tauN_reco.at(iTauN));
            
            sprintf(brName, "hepTop_tau%dratio_reco", iTauN);
            tree->Branch(brName, &vv_hepTop_tauNratio_reco.at(iTauN));
        }
        
        
        this->hepTop_CN_max = hepTop_CN_max;
        
        vv_hepTop_CN_reco.resize(hepTop_CN_max+1, {});
        
        for(int iCN = 0; iCN <= hepTop_CN_max; iCN++)
        {
            char brName[1000];
            
            sprintf(brName, "hepTop_C%d_reco", iCN);
            tree->Branch(brName, &vv_hepTop_CN_reco.at(iCN));
        }
        
        
        //
        tree->Branch("h2_hepTop_fracE_phiEtaPlane_reco", &v_h2_hepTop_fracE_phiEtaPlane_reco);
        tree->Branch("h2_hepTop_track_fracE_phiEtaPlane_reco", &v_h2_hepTop_track_fracE_phiEtaPlane_reco);
        tree->Branch("h2_hepTop_photon_fracE_phiEtaPlane_reco", &v_h2_hepTop_photon_fracE_phiEtaPlane_reco);
        tree->Branch("h2_hepTop_neutralHad_fracE_phiEtaPlane_reco", &v_h2_hepTop_neutralHad_fracE_phiEtaPlane_reco);
        
        tree->Branch("h2_hepTop_boosted_fracE_phiEtaPlane_reco", &v_h2_hepTop_boosted_fracE_phiEtaPlane_reco);
        tree->Branch("h2_hepTop_boosted_track_fracE_phiEtaPlane_reco", &v_h2_hepTop_boosted_track_fracE_phiEtaPlane_reco);
        tree->Branch("h2_hepTop_boosted_photon_fracE_phiEtaPlane_reco", &v_h2_hepTop_boosted_photon_fracE_phiEtaPlane_reco);
        tree->Branch("h2_hepTop_boosted_neutralHad_fracE_phiEtaPlane_reco", &v_h2_hepTop_boosted_neutralHad_fracE_phiEtaPlane_reco);
        
        tree->Branch("h2_hepTop_boosted_rescaled_fracE_phiEtaPlane_reco", &v_h2_hepTop_boosted_rescaled_fracE_phiEtaPlane_reco);
        tree->Branch("h2_hepTop_boosted_rescaled_track_fracE_phiEtaPlane_reco", &v_h2_hepTop_boosted_rescaled_track_fracE_phiEtaPlane_reco);
        tree->Branch("h2_hepTop_boosted_rescaled_photon_fracE_phiEtaPlane_reco", &v_h2_hepTop_boosted_rescaled_photon_fracE_phiEtaPlane_reco);
        tree->Branch("h2_hepTop_boosted_rescaled_neutralHad_fracE_phiEtaPlane_reco", &v_h2_hepTop_boosted_rescaled_neutralHad_fracE_phiEtaPlane_reco);
        
        tree->Branch("h2_hepTop_topRestFrame_fracE_phiEtaPlane_reco", &v_h2_hepTop_topRestFrame_fracE_phiEtaPlane_reco);
        tree->Branch("h2_hepTop_topRestFrame_track_fracE_phiEtaPlane_reco", &v_h2_hepTop_topRestFrame_track_fracE_phiEtaPlane_reco);
        tree->Branch("h2_hepTop_topRestFrame_photon_fracE_phiEtaPlane_reco", &v_h2_hepTop_topRestFrame_photon_fracE_phiEtaPlane_reco);
        tree->Branch("h2_hepTop_topRestFrame_neutralHad_fracE_phiEtaPlane_reco", &v_h2_hepTop_topRestFrame_neutralHad_fracE_phiEtaPlane_reco);
        
        tree->Branch("h2_hepTop_topRestFrame_rescaled_fracE_phiEtaPlane_reco", &v_h2_hepTop_topRestFrame_rescaled_fracE_phiEtaPlane_reco);
        tree->Branch("h2_hepTop_topRestFrame_rescaled_track_fracE_phiEtaPlane_reco", &v_h2_hepTop_topRestFrame_rescaled_track_fracE_phiEtaPlane_reco);
        tree->Branch("h2_hepTop_topRestFrame_rescaled_photon_fracE_phiEtaPlane_reco", &v_h2_hepTop_topRestFrame_rescaled_photon_fracE_phiEtaPlane_reco);
        tree->Branch("h2_hepTop_topRestFrame_rescaled_neutralHad_fracE_phiEtaPlane_reco", &v_h2_hepTop_topRestFrame_rescaled_neutralHad_fracE_phiEtaPlane_reco);
    }
    
    
    void clear()
    {
        //
        hadTop_n_truth = 0;
        v_hadTop_pT_truth.clear();
        v_hadTop_eta_truth.clear();
        v_hadTop_phi_truth.clear();
        v_hadTop_m_truth.clear();
        v_hadTop_E_truth.clear();
        v_hadTop_px_truth.clear();
        v_hadTop_py_truth.clear();
        v_hadTop_pz_truth.clear();
        
        hadTopB_n_truth = 0;
        v_hadTopB_pT_truth.clear();
        v_hadTopB_eta_truth.clear();
        v_hadTopB_phi_truth.clear();
        v_hadTopB_E_truth.clear();
        v_hadTopB_px_truth.clear();
        v_hadTopB_py_truth.clear();
        v_hadTopB_pz_truth.clear();
        v_hadTopB_Wq1deltaR_truth.clear();
        v_hadTopB_Wq2deltaR_truth.clear();
        v_hadTopB_hadTopDeltaR_truth.clear();
        
        hadTopW_n_truth = 0;
        v_hadTopW_pT_truth.clear();
        v_hadTopW_eta_truth.clear();
        v_hadTopW_phi_truth.clear();
        v_hadTopW_E_truth.clear();
        v_hadTopW_px_truth.clear();
        v_hadTopW_py_truth.clear();
        v_hadTopW_pz_truth.clear();
        
        v_Wq1_pT_truth.clear();
        v_Wq1_eta_truth.clear();
        v_Wq1_phi_truth.clear();
        v_Wq1_E_truth.clear();
        v_Wq1_px_truth.clear();
        v_Wq1_py_truth.clear();
        v_Wq1_pz_truth.clear();
        v_Wq1_pid_truth.clear();
        v_Wq1_Wq2deltaR_truth.clear();
        v_Wq1_hadTopDeltaR_truth.clear();
        
        v_Wq2_pT_truth.clear();
        v_Wq2_eta_truth.clear();
        v_Wq2_phi_truth.clear();
        v_Wq2_E_truth.clear();
        v_Wq2_px_truth.clear();
        v_Wq2_py_truth.clear();
        v_Wq2_pz_truth.clear();
        v_Wq2_pid_truth.clear();
        v_Wq2_hadTopDeltaR_truth.clear();
        
        v_cosThetaStar_truth.clear();
        v_zk_truth.clear();
        v_zb_truth.clear();
        
        
        //
        lepTop_n_truth = 0;
        v_lepTop_pT_truth.clear();
        v_lepTop_eta_truth.clear();
        v_lepTop_phi_truth.clear();
        v_lepTop_m_truth.clear();
        v_lepTop_E_truth.clear();
        v_lepTop_px_truth.clear();
        v_lepTop_py_truth.clear();
        v_lepTop_pz_truth.clear();
        
        v_lepTopVis_pT_truth.clear();
        v_lepTopVis_eta_truth.clear();
        v_lepTopVis_phi_truth.clear();
        v_lepTopVis_m_truth.clear();
        v_lepTopVis_E_truth.clear();
        v_lepTopVis_px_truth.clear();
        v_lepTopVis_py_truth.clear();
        v_lepTopVis_pz_truth.clear();
        
        v_lepTopB_pT_truth.clear();
        v_lepTopB_eta_truth.clear();
        v_lepTopB_phi_truth.clear();
        v_lepTopB_E_truth.clear();
        v_lepTopB_px_truth.clear();
        v_lepTopB_py_truth.clear();
        v_lepTopB_pz_truth.clear();
        v_lepTopB_lepTopDeltaR_truth.clear();
        v_lepTopB_lepTopVisDeltaR_truth.clear();
        
        v_lepTopW_pT_truth.clear();
        v_lepTopW_eta_truth.clear();
        v_lepTopW_phi_truth.clear();
        v_lepTopW_E_truth.clear();
        v_lepTopW_px_truth.clear();
        v_lepTopW_py_truth.clear();
        v_lepTopW_pz_truth.clear();
        
        v_Wlep_pT_truth.clear();
        v_Wlep_eta_truth.clear();
        v_Wlep_phi_truth.clear();
        v_Wlep_E_truth.clear();
        v_Wlep_px_truth.clear();
        v_Wlep_py_truth.clear();
        v_Wlep_pz_truth.clear();
        v_Wlep_pid_truth.clear();
        v_Wlep_lepTopDeltaR_truth.clear();
        v_Wlep_lepTopVisDeltaR_truth.clear();
        
        v_lepTop_deltaRbl_truth.clear();
        v_lepTop_mbl_truth.clear();
        v_zl_truth.clear();
        
        
        //
        c_n_truth = 0;
        v_c_pT_truth.clear();
        v_c_eta_truth.clear();
        v_c_phi_truth.clear();
        v_c_E_truth.clear();
        v_c_px_truth.clear();
        v_c_py_truth.clear();
        v_c_pz_truth.clear();
        
        
        //
        b_n_truth = 0;
        v_b_pT_truth.clear();
        v_b_eta_truth.clear();
        v_b_phi_truth.clear();
        v_b_E_truth.clear();
        v_b_px_truth.clear();
        v_b_py_truth.clear();
        v_b_pz_truth.clear();
        
        
        //
        hepTop_n_reco = 0;
        
        v_hepTop_raw_pT_reco.clear();
        v_hepTop_raw_eta_reco.clear();
        v_hepTop_raw_phi_reco.clear();
        v_hepTop_raw_E_reco.clear();
        v_hepTop_raw_px_reco.clear();
        v_hepTop_raw_py_reco.clear();
        v_hepTop_raw_pz_reco.clear();
        v_hepTop_raw_m_reco.clear();
        
        v_hepTop_pT_reco.clear();
        v_hepTop_eta_reco.clear();
        v_hepTop_phi_reco.clear();
        v_hepTop_E_reco.clear();
        v_hepTop_px_reco.clear();
        v_hepTop_py_reco.clear();
        v_hepTop_pz_reco.clear();
        v_hepTop_m_reco.clear();
        
        v_hepTop_nExcSubJet_reco.clear();
        
        v_hepTop_subJet12_m_reco.clear();
        v_hepTop_subJet23_m_reco.clear();
        v_hepTop_subJet31_m_reco.clear();
        
        v_hepTop_subJet123_m_reco.clear();
        
        v_hepTop_frec_reco.clear();
        
        v_hepTop_nSubJetBtagged_reco.clear();
        v_hepTop_nSubJetBmatched_reco.clear();
        v_hepTop_subJet1B_deltaR_reco.clear();
        v_hepTop_subJet2B_deltaR_reco.clear();
        v_hepTop_subJet3B_deltaR_reco.clear();
        
        v_hepTop_nBinFatJet_reco.clear();
        v_hepTop_nBtaggedJetInFatJet_reco.clear();
        
        v_hepTop_showerDecon_chi_reco.clear();
        v_hepTop_showerDecon_logChi_reco.clear();
        
        v_hepTop_zk_reco.clear();
        v_hepTop_zb_reco.clear();
        v_hepTop_cosThetaStar_reco.clear();
        
        v_hepTop_zl_reco.clear();
        
        v_hepTop_lep_subJetLep_genLep_deltaR_reco.clear();
        v_hepTop_lep_subJetLep_genB_deltaR_reco.clear();
        v_hepTop_lep_subJetB_genB_deltaR_reco.clear();
        v_hepTop_lep_subJetB_genLep_deltaR_reco.clear();
        
        v_hepTop_lepSubJet1_miniIso_reco.clear();
        v_hepTop_lepSubJet2_miniIso_reco.clear();
        
        v_hepTop_nearestGenHadTop_index.clear();
        v_hepTop_nearestGenLepTop_index.clear();
        
        v_hepTop_genHadTop_deltaR_reco.clear();
        v_hepTop_genLepTop_deltaR_reco.clear();
        
        v_hepTop_nGenTopConstiMatched_reco.clear();
        
        v_hepTop_isMayBeTop_reco.clear();
        v_hepTop_isTagged_reco.clear();
        
        for(int iTauN = 0; iTauN <= hepTop_tauN_max; iTauN++)
        {
            vv_hepTop_tauN_reco.at(iTauN).clear();
            vv_hepTop_tauNratio_reco.at(iTauN).clear();
        }
        
        for(int iCN = 0; iCN <= hepTop_CN_max; iCN++)
        {
            vv_hepTop_CN_reco.at(iCN).clear();
        }
        
        v_h2_hepTop_fracE_phiEtaPlane_reco.clear();
        v_h2_hepTop_track_fracE_phiEtaPlane_reco.clear();
        v_h2_hepTop_photon_fracE_phiEtaPlane_reco.clear();
        v_h2_hepTop_neutralHad_fracE_phiEtaPlane_reco.clear();
        
        v_h2_hepTop_boosted_fracE_phiEtaPlane_reco.clear();
        v_h2_hepTop_boosted_track_fracE_phiEtaPlane_reco.clear();
        v_h2_hepTop_boosted_photon_fracE_phiEtaPlane_reco.clear();
        v_h2_hepTop_boosted_neutralHad_fracE_phiEtaPlane_reco.clear();
        
        v_h2_hepTop_boosted_rescaled_fracE_phiEtaPlane_reco.clear();
        v_h2_hepTop_boosted_rescaled_track_fracE_phiEtaPlane_reco.clear();
        v_h2_hepTop_boosted_rescaled_photon_fracE_phiEtaPlane_reco.clear();
        v_h2_hepTop_boosted_rescaled_neutralHad_fracE_phiEtaPlane_reco.clear();
        
        v_h2_hepTop_topRestFrame_fracE_phiEtaPlane_reco.clear();
        v_h2_hepTop_topRestFrame_track_fracE_phiEtaPlane_reco.clear();
        v_h2_hepTop_topRestFrame_photon_fracE_phiEtaPlane_reco.clear();
        v_h2_hepTop_topRestFrame_neutralHad_fracE_phiEtaPlane_reco.clear();
        
        v_h2_hepTop_topRestFrame_rescaled_fracE_phiEtaPlane_reco.clear();
        v_h2_hepTop_topRestFrame_rescaled_track_fracE_phiEtaPlane_reco.clear();
        v_h2_hepTop_topRestFrame_rescaled_photon_fracE_phiEtaPlane_reco.clear();
        v_h2_hepTop_topRestFrame_rescaled_neutralHad_fracE_phiEtaPlane_reco.clear();
    }
    
    
    void fill()
    {
        tree->Fill();
    }
    
    
    void write()
    {
        tree->Write();
    }
    
    
    void freeMemory()
    {
        delete tree;
    }
};



GenParticle* getFirstCopy(TClonesArray *br_Particle, GenParticle* genParticle)
{
    int id = genParticle->PID;
    
    int mother1_index = genParticle->M1;
    int mother2_index = genParticle->M2;
    
    GenParticle *mother1 = 0;
    GenParticle *mother2 = 0;
    
    if(mother1_index >= 0 )
    {
        mother1 = (GenParticle*) br_Particle->At(mother1_index);
    }
    
    if(mother2_index >= 0)
    {
        mother2 = (GenParticle*) br_Particle->At(mother2_index);
    }
    
    // Recurse if mother is the same
    if(mother1 && mother1->PID == id)
    {
        return getFirstCopy(br_Particle, mother1);
    }
    
    else if(mother2 && mother2->PID == id)
    {
        return getFirstCopy(br_Particle, mother2);
    }
    
    return genParticle;
}


GenParticle* getLastCopy(TClonesArray *br_Particle, GenParticle* genParticle)
{
    int id = genParticle->PID;
    
    int daughter1_index = genParticle->D1;
    int daughter2_index = genParticle->D2;
    
    GenParticle *daughter1 = 0;
    GenParticle *daughter2 = 0;
    
    if(daughter1_index >= 0 )
    {
        daughter1 = (GenParticle*) br_Particle->At(daughter1_index);
    }
    
    if(daughter2_index >= 0)
    {
        daughter2 = (GenParticle*) br_Particle->At(daughter2_index);
    }
    
    // Recurse if daughter is the same
    if(daughter1 && daughter1->PID == id)
    {
        return getLastCopy(br_Particle, daughter1);
    }
    
    else if(daughter2 && daughter2->PID == id)
    {
        return getLastCopy(br_Particle, daughter2);
    }
    
    return genParticle;
}


bool isHadronicTop(TClonesArray *br_Particle, GenParticle *genParticle)
{
    genParticle = getLastCopy(br_Particle, genParticle);
    
    int id = genParticle->PID;
    int status = genParticle->Status;
    int daughter1_index = genParticle->D1;
    int daughter2_index = genParticle->D2;
    
    GenParticle *daughter1 = 0;
    GenParticle *daughter2 = 0;
    
    if(daughter1_index >= 0 )
    {
        daughter1 = (GenParticle*) br_Particle->At(daughter1_index);
    }
    
    if(daughter2_index >= 0)
    {
        daughter2 = (GenParticle*) br_Particle->At(daughter2_index);
    }
    
    // Recurse if daughter is a W
    if(daughter1 && abs(daughter1->PID) == 24)
    {
        return isHadronicTop(br_Particle, daughter1);
    }
    
    else if(daughter2 && abs(daughter2->PID) == 24)
    {
        return isHadronicTop(br_Particle, daughter2);
    }
    
    
    bool isHadronic = true;
    
    if(
        daughter1 && daughter2 &&
        abs(daughter1->PID) >= 11 && abs(daughter1->PID) <= 16 &&
        abs(daughter2->PID) >= 11 && abs(daughter2->PID) <= 16
    )
    {
        isHadronic = false;
    }
    
    return isHadronic;
}


double getDistance2(CLHEP::HepLorentzVector obj1_4mom, CLHEP::HepLorentzVector obj2_4mom, int index)
{
    double deltaR = obj1_4mom.deltaR(obj2_4mom);
    
    double dist2 = min(pow(obj1_4mom.perp(), index), pow(obj2_4mom.perp(), index)) * pow(deltaR, 2);
    
    return dist2;
}


double getDistance(CLHEP::HepLorentzVector obj1_4mom, CLHEP::HepLorentzVector obj2_4mom, int index)
{
    return sqrt(getDistance2(obj1_4mom, obj2_4mom, index));
}


std::pair <CLHEP::HepLorentzVector, CLHEP::HepLorentzVector> getClosestPair(std::vector <CLHEP::HepLorentzVector> v_obj_4mom)
{
    if(v_obj_4mom.size() < 2)
    {
        printf("Error in getClosestPair(...): Input vector size must be at least 2. \n");
        exit(EXIT_FAILURE);
    }
    
    CLHEP::HepLorentzVector obj1_4mom = v_obj_4mom.at(0);
    CLHEP::HepLorentzVector obj2_4mom = v_obj_4mom.at(1);
    
    // Get the kT distance
    double dist2_min = getDistance2(obj1_4mom, obj2_4mom, 2);
    
    for(int iObj1 = 0; iObj1 < v_obj_4mom.size(); iObj1++)
    {
        for(int iObj2 = iObj1+1; iObj2 < v_obj_4mom.size(); iObj2++)
        {
            double dist2 = getDistance2(v_obj_4mom.at(iObj1), v_obj_4mom.at(iObj2), 2);
            
            if(dist2 < dist2_min)
            {
                dist2_min = dist2;
                
                obj1_4mom = v_obj_4mom.at(iObj1);
                obj2_4mom = v_obj_4mom.at(iObj2);
            }
        }
    }
    
    std::pair <CLHEP::HepLorentzVector, CLHEP::HepLorentzVector> p_objPair_4mom(obj1_4mom, obj2_4mom);
    
    return p_objPair_4mom;
}


GenParticle* selectDaughter(TClonesArray *br_Particle, GenParticle *genParticle, int selectPID, bool absPID)
{
    genParticle = getLastCopy(br_Particle, genParticle);
    
    int daughter1_index = genParticle->D1;
    int daughter2_index = genParticle->D2;
    
    int daughter1_absPID = -1;
    int daughter2_absPID = -1;
    
    GenParticle *daughter1 = 0;
    GenParticle *daughter2 = 0;
    
    if(daughter1_index >= 0 )
    {
        daughter1 = (GenParticle*) br_Particle->At(daughter1_index);
        
        daughter1_absPID = (absPID)? abs(daughter1->PID): daughter1->PID;
    }
    
    if(daughter2_index >= 0)
    {
        daughter2 = (GenParticle*) br_Particle->At(daughter2_index);
        
        daughter2_absPID = (absPID)? abs(daughter2->PID): daughter2->PID;
    }
    
    selectPID = (absPID)? abs(selectPID): selectPID;
    
    GenParticle *daughter = 0;
    
    if(daughter1 && daughter1_absPID == selectPID)
    {
        daughter = daughter1;
    }
    
    else if(daughter2 && daughter2_absPID == selectPID)
    {
        daughter = daughter2;
    }
    
    //daughter = getLastCopy(daughter);
    
    return daughter;
}


template <typename T1> CLHEP::HepLorentzVector delphesObjToHepLorentzVector(T1 *obj)
{
    CLHEP::HepLorentzVector obj_4mom;
    obj_4mom.setT(obj->P4().E());
    obj_4mom.setX(obj->P4().Px());
    obj_4mom.setY(obj->P4().Py());
    obj_4mom.setZ(obj->P4().Pz());
    
    return obj_4mom;
}


CLHEP::HepLorentzVector TLorentzVectorToHepLorentzVector(TLorentzVector obj)
{
    CLHEP::HepLorentzVector obj_4mom;
    obj_4mom.setT(obj.E());
    obj_4mom.setX(obj.Px());
    obj_4mom.setY(obj.Py());
    obj_4mom.setZ(obj.Pz());
    
    return obj_4mom;
}


template <typename T1> std::vector <CLHEP::HepLorentzVector> delphesObjVecToHepLorentzVector(std::vector <T1*> v_obj)
{
    std::vector <CLHEP::HepLorentzVector> v_obj_4mom;
    
    for(int iObj = 0; iObj < v_obj.size(); iObj++)
    {
        v_obj_4mom.push_back(delphesObjToHepLorentzVector(v_obj.at(iObj)));
    }
    
    return v_obj_4mom;
}


//template <typename T1> std::vector <CLHEP::HepLorentzVector> TClonesArrayToHepLorentzVectorArray(std::vector <T1*> *v_obj)
//{
//    std::vector <CLHEP::HepLorentzVector> v_obj_4mom;
//    
//    for(int iObj = 0; iObj < v_obj->GetEntries(); iObj++)
//    {
//        v_obj_4mom.push_back(delphesObjToHepLorentzVector(v_obj->at(iObj)))
//    }
//    
//    return v_obj_4mom;
//}


CLHEP::HepLorentzVector PseudoJetToHepLorentzVector(fastjet::PseudoJet pseudoJet)
{
    CLHEP::HepLorentzVector obj_4mom;
    obj_4mom.setT(pseudoJet.e());
    obj_4mom.setX(pseudoJet.px());
    obj_4mom.setY(pseudoJet.py());
    obj_4mom.setZ(pseudoJet.pz());
    
    return obj_4mom;
}


double getIso(
    CLHEP::HepLorentzVector obj_4mom,
    double deltaR_max,
    double isoObj_pTmin,
    std::vector <CLHEP::HepLorentzVector> v_isoObj_4mom
)
{
    double isoVar = 0;
    
    for(int iIsoObj = 0; iIsoObj < v_isoObj_4mom.size(); iIsoObj++)
    {
        CLHEP::HepLorentzVector isoObj_4mom = v_isoObj_4mom.at(iIsoObj);
        
        if(isoObj_4mom.perp() < isoObj_pTmin)
        {
            continue;
        }
        
        double deltaR = obj_4mom.deltaR(isoObj_4mom);
        
        if(deltaR < deltaR_max)
        {
            isoVar += isoObj_4mom.perp();
        }
        
        //printf("%s \n", typeid(isoObj).name());
        //fflush(stdout);
    }
    
    isoVar -= obj_4mom.perp();
    
    if(isoVar < 0)
    {
        isoVar = 0;
    }
    
    
    return isoVar;
}


std::pair <std::pair <int, int>, double> findMatrixMinimum(TMatrixD matrix)
{
    int minRow = -1;
    int minCol = -1;
    
    double minVal = matrix.Max() + 1;
    
    for(int iRow = 0; iRow < matrix.GetNrows(); iRow++)
    {
        for(int iCol = 0; iCol < matrix.GetNcols(); iCol++)
        {
            if(matrix(iRow, iCol) < minVal)
            {
                minVal = matrix(iRow, iCol);
                
                minRow = iRow;
                minCol = iCol;
            }
        }
    }
    
    std::pair <std::pair <int, int>, double> result = std::make_pair(
        std::make_pair(minRow, minCol),
        minVal
    );
    
    return result;
}


void deleteMatrixRow(TMatrixD &matrix, int rowIdx)
{
    //printf("Entering deleteMatrixRow(...) \n");
    
    if(rowIdx < 0)
    {
        printf("Error in deleteMatrixRow(...): Invalid row index (%d). \n", rowIdx);
        exit(EXIT_FAILURE);
    }
    
    //printf("Matrix before row deletion: \n");
    //matrix.Print();
    
    int nRow = matrix.GetNrows();
    int nCol = matrix.GetNcols();
    
    if(nRow == 1)
    {
        matrix.ResizeTo(0, 0);
    }
    
    else
    {
        int rowSkipped = 0;
        
        for(int iRow = 0; iRow < nRow-1; iRow++)
        {
            if(iRow >= rowIdx)
            {
                rowSkipped = 1;
            }
            
            for(int iCol = 0; iCol < nCol; iCol++)
            {
                //printf("In deleteMatrixRow(...): iRow %d/%d, iCol %d:%d \n", iRow, nRow-1, iCol, nCol-1);
                
                matrix(iRow, iCol) = matrix(iRow+rowSkipped, iCol);
            }
        }
        
        matrix.ResizeTo(nRow-1, nCol);
    }
    
    //printf("Matrix after row deletion: \n");
    //matrix.Print();
}


void deleteMatrixCol(TMatrixD &matrix, int colIdx)
{
    //printf("Entering deleteMatrixCol(...) \n");
    
    if(colIdx < 0)
    {
        printf("Error in deleteMatrixCol(...): Invalid col index (%d). \n", colIdx);
        exit(EXIT_FAILURE);
    }
    
    //printf("Matrix before column deletion: \n");
    //matrix.Print();
    
    int nRow = matrix.GetNrows();
    int nCol = matrix.GetNcols();
    
    if(nCol == 1)
    {
        matrix.ResizeTo(0, 0);
    }
    
    else
    {
        for(int iRow = 0; iRow < nRow; iRow++)
        {
            for(int iCol = 0; iCol < nCol-1; iCol++)
            {
                int colSkipped = 0;
                
                if(iCol >= colIdx)
                {
                    colSkipped = 1;
                }
                
                //printf("In deleteMatrixCol(...): iRow %d/%d, iCol %d:%d \n", iRow, nRow-1, iCol, nCol-1);
                
                matrix(iRow, iCol) = matrix(iRow, iCol+colSkipped);
            }
        }
        
        matrix.ResizeTo(nRow, nCol-1);
    }
    
    //printf("Matrix after column deletion: \n");
    //matrix_mod.Print();
}


void deleteMatrixRowCol(TMatrixD &matrix, int rowIdx, int colIdx)
{
    //printf("Entering deleteMatrixRowCol(...) \n");
    //fflush(stdout);
    
    //printf("Matrix before row and column deletion: \n");
    //matrix.Print();
    
    if(!matrix.GetNrows())
    {
        return;
    }
    
    deleteMatrixRow(matrix, rowIdx);
    
    if(!matrix.GetNcols())
    {
        return;
    }
    
    deleteMatrixCol(matrix, colIdx);
    
    //printf("Matrix after row and column deletion: \n");
    //matrix.Print();
}


double runShowerDeconstruction(Deconstruction::Deconstruct *deconstruct, fastjet::PseudoJet jet)
{
    if(jet.constituents().size() == 0)
    {
        return -999;
    }
    
    fastjet::JetDefinition microjet_def(fastjet::cambridge_algorithm, 0.2); // make sub-jets with R=0.2
    fastjet::ClusterSequence microjet_cs(jet.constituents(), microjet_def);
    double pt_cut = 20; // cut on sub-jet pT of 20 GeV, for example
    
    // make sub-jets
    std::vector <fastjet::PseudoJet> microjets = fastjet::sorted_by_pt(microjet_cs.inclusive_jets(pt_cut));
    
    // if there are too many subjets, take only the leading 9 sub-jets, to limit time taken in SD
    if(microjets.size() > 9)
    {
        microjets.erase(microjets.begin() + (int) 9, microjets.begin() + microjets.size());
    }
    
    double chi = -100; // to hold the result of SD
    
    // chi is the ratio of signal and background weights
    // Deconstruct also returns the sum of signal and background weights for convenience
    double wSignal = -100;
    double wBackground = -100;
    
    try
    {
      chi = deconstruct->deconstruct(microjets, wSignal, wBackground);
    }
    
    catch(Deconstruction::Exception &e)
    {
        std::cout << "Exception while running SD: " << e.what() << std::endl;
    }
    
    chi = deconstruct->deconstruct(microjets, wSignal, wBackground);
    
    return chi;
    
    //// now return the logarithm of chi
    //double lchi = -100;
    //
    //if (chi > 0)
    //{
    //    lchi = std::log(chi);
    //}
    //
    //return lchi;
}


bool isBtagged_parametrized(CLHEP::HepLorentzVector obj_4mom, int pid)
{
    bool isBtagged = false;
    
    std::uniform_real_distribution<> randDist(0.0, 1.0);
    
    // udsg
    if(pid == 0)
    {
        double pT = obj_4mom.perp();
        double eff = 0.01+0.000038*pT;
        
        double randNum = randDist(_randomEngine);
        //printf("%0.4f \n", randNum);
        
        isBtagged = randNum < eff;
    }
    
    // c
    else if(pid == 4)
    {
        double pT = obj_4mom.perp();
        double eff = 0.25*tanh(0.018*pT)*(1/(1+ 0.0013*pT));
        
        double randNum = randDist(_randomEngine);
        //printf("%0.4f \n", randNum);
        
        isBtagged = randNum < eff;
    }
    
    // b
    else if(pid == 5)
    {
        double pT = obj_4mom.perp();
        double eff = 0.85*tanh(0.0025*pT)*(25.0/(1+0.063*pT));
        
        double randNum = randDist(_randomEngine);
        //printf("%0.4f \n", randNum);
        
        isBtagged = randNum < eff;
    }
    
    return isBtagged;
}


double getRapidityDeltaR(
   CLHEP::HepLorentzVector obj1,
   CLHEP::HepLorentzVector obj2
)
{
    double dy = obj1.rapidity() - obj2.rapidity();
    double dPhi = obj1.v().deltaPhi(obj2.v());
    
    double deltaR = sqrt(dy*dy + dPhi*dPhi);
    
    return deltaR;
}


double getRapidityDeltaR(
   TLorentzVector obj1,
   TLorentzVector obj2
)
{
    return getRapidityDeltaR(
        TLorentzVectorToHepLorentzVector(obj1),
        TLorentzVectorToHepLorentzVector(obj2)
    );
}


// Will return {dRmin1, ... dRminN} of size v_obj1_4mom.size()
std::vector <double> getMinDeltaR(
    std::vector <CLHEP::HepLorentzVector> v_obj1_4mom,
    std::vector <CLHEP::HepLorentzVector> v_obj2_4mom,
    TMatrixD &mat_deltaR_result,
    bool useRapidity = false,
    int defaultVal = _defaultVal1
)
{
    int nObj1 = v_obj1_4mom.size();
    int nObj2 = v_obj2_4mom.size();
    
    TMatrixD tmat_deltaR(nObj1, nObj2);
    
    for(int iObj1 = 0; iObj1 < nObj1; iObj1++)
    {
        for(int iObj2 = 0; iObj2 < nObj2; iObj2++)
        {
            double deltaR = 0;
            
            if(useRapidity)
            {
                deltaR = getRapidityDeltaR(v_obj1_4mom.at(iObj1), v_obj2_4mom.at(iObj2));
            }
            
            else
            {
                v_obj1_4mom.at(iObj1).deltaR(v_obj2_4mom.at(iObj2));
            }
            
            tmat_deltaR(iObj1, iObj2) = deltaR;
        }
    }
    
    mat_deltaR_result.ResizeTo(nObj1, nObj2);
    
    mat_deltaR_result = tmat_deltaR;
    
    std::vector <double> v_deltaR_min(nObj1, defaultVal);
    
    int nIter = std::min(nObj1, nObj2);
    
    for(int iIter = 0; iIter < nIter; iIter++)
    {
        std::pair <std::pair <int, int>, double> matrixMinResult = findMatrixMinimum(tmat_deltaR);
        
        int minRow = matrixMinResult.first.first;
        int minCol = matrixMinResult.first.second;
        
        double minVal = matrixMinResult.second;
        
        if(minVal == defaultVal)
        {
            break;
        }
        
        v_deltaR_min.at(minRow) = minVal;
        
        //printf("tmat_deltaR before masking: \n");
        //tmat_deltaR.Print();
        
        // Mask minRow and minCol
        TMatrixDRow(tmat_deltaR, minRow).Assign(defaultVal);
        TMatrixDColumn(tmat_deltaR, minCol).Assign(defaultVal);
        
        //printf("tmat_deltaR after masking: \n");
        //tmat_deltaR.Print();
        
        //v_deltaR_min.at(iIter) = minVal;
        //
        //deleteMatrixRowCol(tmat_deltaR, minRow, minCol);
        //
        //if(!tmat_deltaR.GetNrows() || !tmat_deltaR.GetNcols())
        //{
        //    break;
        //}
    }
    
    return v_deltaR_min;
}


double getFastJetMiniIso(
    fastjet::PseudoJet fj_obj,
    std::vector <fastjet::PseudoJet> v_fj_isoObj,
    bool subtractSig = true
)
{
    double miniIso = 0;
    
    if(!fj_obj.perp())
    {
        return miniIso;
    }
    
    double isoDR = 0.2;
    
    if(fj_obj.perp() > 50)
    {
        isoDR = 10.0 / fj_obj.perp();
    }
    
    if(fj_obj.perp() > 200)
    {
        isoDR = 0.05;
    }
    
    for(int iObj = 0; iObj < v_fj_isoObj.size(); iObj++)
    {
        double dR = fj_obj.delta_R(v_fj_isoObj.at(iObj));
        
        if(dR < isoDR)
        {
            miniIso += v_fj_isoObj.at(iObj).perp();
        }
    }
    
    if(subtractSig)
    {
        miniIso -= fj_obj.perp();
    }
    
    miniIso /= fj_obj.perp();
    
    return miniIso;
}


/*void getPCAtransformedFromTH2(
    TH2F *h2_hist,
    TMatrixD mat_data,
    TMatrixD &mat_data_pca
)
{
    mat_data_pca.ResizeTo(mat_data.GetNrows(), mat_data.GetNcols());
    mat_data_pca = mat_data;
    
    TMatrixD mat_cov(2, 2);
    mat_cov(0, 0) = h2_hist->GetCovariance(2, 2);
    mat_cov(1, 1) = h2_hist->GetCovariance(1, 1);
    mat_cov(0, 1) = h2_hist->GetCovariance();
    mat_cov(1, 0) = h2_hist->GetCovariance();
    
    
    TVectorD v_eigVal(2);
    TMatrixD mat_eigVec(2, 2);
    
    TMatrixD mat_rot(2, 2);
    
    try
    {
        mat_eigVec = mat_cov.EigenVectors(v_eigVal);
    }
    
    catch(...)
    {
        printf("Error in getPCAtransformedFromTH2(...): Cannot get eigen values and vectors. \n");
        
        printf("Cov. matrix: \n");
        mat_cov.Print();
        
        fflush(stdout);
        fflush(stderr);
    }
    
    // By default each row is an eigen-vector
    // Transpose so that each column in an eigen-vector
    mat_eigVec.T();
    
    mat_data_pca.Mult(mat_eigVec, mat_data); 
}*/


// {..., (dEta, dPhi), ... } --> {..., (dEta_trans, dPhi_trans), ...}
std::vector <std::vector <double> > getTransformedDetaDphi(
    std::vector <fastjet::PseudoJet> v_pseudoJet,
    fastjet::PseudoJet pseudoJet_ref,
    TVectorD direc1,
    TVectorD direc2,
    TVectorD finalTranslation
)
{
    int nConsti = v_pseudoJet.size();
    
    TMatrixD mat_rotate(2, 2);
    TMatrixD mat_reflect(2, 2);
    
    TMatrixD mat_DetaDphi(2, nConsti);
    
    for(int iConsti = 0; iConsti < nConsti; iConsti++)
    {
        fastjet::PseudoJet consti = v_pseudoJet.at(iConsti);
        
        double dEta = consti.eta() - pseudoJet_ref.eta();
        double dPhi = pseudoJet_ref.delta_phi_to(consti);
        
        mat_DetaDphi(0, iConsti) = dEta;
        mat_DetaDphi(1, iConsti) = dPhi;
    }
    
    double direc1_norm = sqrt(direc1.Norm2Sqr());
    double direc2_norm = sqrt(direc2.Norm2Sqr());
    
    bool isReflected = false;
    
    if(direc1_norm)
    {
        direc1 *= (1.0 / direc1_norm);
        
        mat_rotate(0, 0) = +direc1(0);
        mat_rotate(0, 1) = +direc1(1);
        
        mat_rotate(1, 0) = -direc1(1);
        mat_rotate(1, 1) = +direc1(0);
        
        mat_DetaDphi = mat_rotate * mat_DetaDphi;
        
        finalTranslation = mat_rotate * finalTranslation;
        
        if(direc2_norm)
        {
            direc2 *= (1.0 / direc2_norm);
            
            // Reflect
            TVectorD direc2_transformed(2);
            direc2_transformed = mat_rotate * direc2;
            
            if(direc2_transformed(1) < 0)
            {
                mat_reflect(0, 0) = +1.0;
                mat_reflect(1, 1) = -1.0;
                
                mat_reflect(1, 0) = 0.0;
                mat_reflect(0, 1) = 0.0;
                
                mat_DetaDphi = mat_reflect * mat_DetaDphi;
                
                isReflected = true;
                finalTranslation(1) *= -1;
            }
        }
    }
    
    
    std::vector <std::vector <double> > v_result(nConsti);
    
    
    //#pragma omp parallel for
    for(int iConsti = 0; iConsti < nConsti; iConsti++)
    {
        std::vector <double> v_temp = {
            mat_DetaDphi(0, iConsti) - finalTranslation(0),
            mat_DetaDphi(1, iConsti) - finalTranslation(1),
        };
        
        // Keep ref-axis in the +ve x-axis
        if(finalTranslation(0) && mat_DetaDphi(0, iConsti) < 0)
        {
            mat_DetaDphi(0, iConsti) *= -1;
        }
        
        v_result.at(iConsti) = v_temp;
    }
    
    return v_result;
}


std::vector <CLHEP::HepLorentzVector> getGStranformed4mom(
    std::vector <fastjet::PseudoJet> v_axis_psJet,
    std::vector <fastjet::PseudoJet> v_psJet
)
{
    // Find the GS axes
    std::vector <CLHEP::Hep3Vector> v_GSaxis;
    
    for(int iAxis = 0; iAxis < v_axis_psJet.size(); iAxis++)
    {
        CLHEP::Hep3Vector GSaxis = PseudoJetToHepLorentzVector(v_axis_psJet.at(iAxis)).v().unit();
        
        for(int iGSaxis = 0; iGSaxis < v_GSaxis.size(); iGSaxis++)
        {
            GSaxis -= GSaxis.dot(v_GSaxis.at(iGSaxis)) * v_GSaxis.at(iGSaxis);
        }
        
        GSaxis = GSaxis.unit();
        
        v_GSaxis.push_back(GSaxis);
    }
    
    
    //printf("GSaxis: \n");
    //
    //for(int iGSaxis = 0; iGSaxis < v_GSaxis.size(); iGSaxis++)
    //{
    //    printf(
    //        "\t %d (%0.2e, %0.2e, %0.2e):  ",
    //        iGSaxis+1,
    //        v_GSaxis.at(iGSaxis).x(), v_GSaxis.at(iGSaxis).y(), v_GSaxis.at(iGSaxis).z()
    //    );
    //    
    //    for(int jGSaxis = 0; jGSaxis < v_GSaxis.size(); jGSaxis++)
    //    {
    //        printf(
    //            "\t %d*%d %0.2e, ",
    //            iGSaxis+1, jGSaxis+1,
    //            v_GSaxis.at(iGSaxis).dot(v_GSaxis.at(jGSaxis))
    //        );
    //    }
    //    
    //    printf("\n");
    //}
    
    
    std::vector <CLHEP::HepLorentzVector> v_GStransformed_4mom(v_psJet.size());
    
    // Transform the 3 momenta
    //#pragma omp parallel for
    for(int iJet = 0; iJet < v_psJet.size(); iJet++)
    {
        CLHEP::HepLorentzVector jet_4mom = PseudoJetToHepLorentzVector(v_psJet.at(iJet));
        
        CLHEP::HepLorentzVector GStransformed_4mom;
        CLHEP::Hep3Vector GStransformed_3mom;;
        
        //#pragma omp parallel for
        for(int iGSaxis = 0; iGSaxis < v_GSaxis.size(); iGSaxis++)
        {
            //printf("\t %d, %0.2e \n", iGSaxis+1, jet_4mom.v().dot(v_GSaxis.at(iGSaxis)));
            
            GStransformed_3mom(iGSaxis) = jet_4mom.v().dot(v_GSaxis.at(iGSaxis));
        }
        
        GStransformed_4mom.setE(jet_4mom.e());
        GStransformed_4mom.setVect(GStransformed_3mom);
        
        v_GStransformed_4mom.at(iJet) = GStransformed_4mom;
        
        //printf(
        //    "Jet %d/%d: "
        //    "(%0.2e, %0.2e, %0.2e, %0.2e) |p| %0.2e, m %0.2e "
        //    "--> "
        //    "(%0.2e, %0.2e, %0.2e, %0.2e) |p| %0.2e, m %0.2e "
        //    "\n ",
        //    
        //    iJet+1, v_psJet.size(),
        //    jet_4mom.e(), jet_4mom.px(), jet_4mom.py(), jet_4mom.pz(), jet_4mom.v().mag(), jet_4mom.m(),
        //    GStransformed_4mom.e(), GStransformed_4mom.px(), GStransformed_4mom.py(), GStransformed_4mom.pz(), GStransformed_4mom.v().mag(), GStransformed_4mom.m()
        //);
    }
    
    //printf("\n\n");
    
    return v_GStransformed_4mom;
}


CLHEP::HepLorentzVector getHepLorentzVectorSum(
    std::vector <CLHEP::HepLorentzVector> v_4mom
)
{
    CLHEP::HepLorentzVector sum_4mom(0, 0, 0, 0);
    
    //#pragma omp parallel for
    for(int iObj = 0; iObj < v_4mom.size(); iObj++)
    {
        sum_4mom += v_4mom.at(iObj);
    }
    
    return sum_4mom;
}


int main(int nArg, char** v_runArg)
{
    //gROOT->ProcessLine(".autodict");
    gROOT->ProcessLine(".L HeaderFiles/CustomRootDict.cc+");
    
    srand(time(0));
    
    std::vector <std::string> v_inputFileName;
    std::string outputDir;
    std::string outputFileName;
    
    int nEvent_max = -1;
    
    bool applySD = true;
    
    try
    {
        boost::program_options::options_description optDesc("Allowed options");
        
        optDesc.add_options()
            ("help", "Help message")
            ("inFileNames", boost::program_options::value<std::vector <std::string> >()->required(), "List of input files")
            ("outDir", boost::program_options::value<std::string>()->required(), "Output directory")
            ("outFileName", boost::program_options::value<std::string>()->required(), "Output file name")
            ("maxEvents", boost::program_options::value<int>(&nEvent_max), "Maximum events to process")
            ("applySD", boost::program_options::value<bool>(&applySD), "Apply soft drop")
        ;
        
        boost::program_options::variables_map varMap;
        boost::program_options::store(boost::program_options::parse_command_line(nArg, v_runArg, optDesc), varMap);
        
        if(varMap.count("help"))
        {
            std::cout << optDesc << "\n";
            return 0;
        }
        
        
        boost::program_options::notify(varMap);
        
        
        if(varMap.count("inFileNames"))
        {
            v_inputFileName = varMap["inFileNames"].as<std::vector <std::string> >();
        }
        
        if(varMap.count("outDir"))
        {
            outputDir = varMap["outDir"].as<std::string>();
        }
        
        if(varMap.count("outFileName"))
        {
            outputFileName = varMap["outFileName"].as<std::string>();
        }
        
        if(varMap.count("maxEvents"))
        {
            nEvent_max = varMap["maxEvents"].as<int>();
        }
        
        if(varMap.count("applySD"))
        {
            applySD = varMap["applySD"].as<bool>();
        }
    }
    
    catch(exception& e)
    {
        std::cerr << "Error: " << e.what() << "\n";
        return EXIT_FAILURE;
    }
    
    catch(...)
    {
        std::cerr << "Exception of unknown type!\n";
        return EXIT_FAILURE;
    }
    
    
    char command[1000];
    
    sprintf(command, "mkdir -p %s", outputDir.c_str());
    system(command);
    
    
    //char *runArg_nEvent_max = v_runArg[2];
    //int nEvent_max = std::stoi(runArg_nEvent_max);
    
    
    gSystem->Load("libDelphes");
    
    TChain *chain = new TChain("Delphes");
    
    //chain->SetMaxVirtualSize(1024 * 1024 * 1024);
    
    for(int iFile = 0; iFile < v_inputFileName.size(); iFile++)
    {
        printf("Adding file: %s \n", v_inputFileName.at(iFile).c_str());
        chain->Add(v_inputFileName.at(iFile).c_str());
    }
    
    printf("\n");
    
    ExRootTreeReader *treeReader = new ExRootTreeReader(chain);
    
    
    char outputFileNameFull[1000];
    //sprintf(outputFileName, "outputTree%s.root", suffix.c_str());
    sprintf(outputFileNameFull, "%s/%s", outputDir.c_str(), outputFileName.c_str());
    
    printf("Output file: %s \n\n", outputFileNameFull);
    
    TFile *outputFile = TFile::Open(outputFileNameFull, "RECREATE");
    OutputInfo *outputInfo = new OutputInfo(_hepTop_tauN_max, _hepTop_CN_max);
    
    
    int nEvent = treeReader->GetEntries();
    printf("Total number of events: %d \n", nEvent);
    
    TClonesArray *br_Particle = treeReader->UseBranch("Particle");
    TClonesArray *br_GenMissingET = treeReader->UseBranch("GenMissingET");
    
    TClonesArray *br_EFlowTrack = treeReader->UseBranch("EFlowTrack");
    TClonesArray *br_EFlowPhoton = treeReader->UseBranch("EFlowPhoton");
    TClonesArray *br_EFlowNeutralHadron = treeReader->UseBranch("EFlowNeutralHadron");
    
    TClonesArray *br_Electron = treeReader->UseBranch("Electron");
    TClonesArray *br_Muon = treeReader->UseBranch("Muon");
    
    TClonesArray *br_MissingET = treeReader->UseBranch("MissingET");
    
    int jet_nMayBeTop = 0;
    int jet_nTopTagged = 0;
    
    int genTop_n = 0;
    
    //int nEvent_max = -1;
    
    if(nEvent_max > 0)
    {
        nEvent = std::min(nEvent, nEvent_max);
    }
    
    AnalysisParameters param(_showerDecon_inputCard);
    
    Deconstruction::TopGluonModel topModel(param);
    Deconstruction::BackgroundModel bkgModel(param);
    Deconstruction::ISRModel isrModel(param);
    
    Deconstruction::Deconstruct showerDecon(param, topModel, bkgModel, isrModel);
    
    int nWprimePos = 0;
    int nWprimeNeg = 0;
    
    for(int iEvent = 0; iEvent < nEvent; iEvent++)
    {
        if((iEvent+1)%1000 == 0 || iEvent == 0 || iEvent+1 == nEvent)
        {
            printf("\n");
            printf("Event %d/%d \n", iEvent+1, nEvent);
        }
        
        //std::cout << "\r" << "Event " << iEvent+1 << "/" << nEvent << " ";
        
        treeReader->ReadEntry(iEvent);
        
        outputInfo->clear();
        
        int nParticle = br_Particle->GetEntries();
        
        int nTrack = br_EFlowTrack->GetEntries();
        int nPhoton = br_EFlowPhoton->GetEntries();
        int nNeutralHad = br_EFlowNeutralHadron->GetEntries();
        
        //printf("[%d/%d] Size of EFlowTrack: %d \n", iEvent, nEvent, nTrack);
        //printf("[%d/%d] Size of EFlowPhoton: %d \n", iEvent, nEvent, nPhoton);
        //printf("[%d/%d] Size of EFlowNeutralHadron: %d \n", iEvent, nEvent, nNeutralHad);
        
        fastjet::Strategy fj_strategy = fastjet::Best;
        fastjet::RecombinationScheme fj_recombScheme = fastjet::E_scheme;
        
        fastjet::JetDefinition *fj_jetDef = new fastjet::JetDefinition(fastjet::antikt_algorithm, _jetR, fj_recombScheme, fj_strategy);
        fastjet::JetDefinition *fj_fatJetDef = new fastjet::JetDefinition(fastjet::cambridge_algorithm, _fatJetR, fj_recombScheme, fj_strategy);
        fastjet::JetDefinition *fj_fatJetExcSubJetDef = new fastjet::JetDefinition(fastjet::kt_algorithm, 1.0, fj_recombScheme, fj_strategy);
        //fastjet::JetDefinition *fj_microJetDef = new fastjet::JetDefinition(fastjet::kt_algorithm, _microJetR, fj_recombScheme, fj_strategy);
        
        std::vector <fastjet::PseudoJet> fj_input;
        
        
        std::vector <int> v_genLepFromW_index;
        
        std::vector <int> v_genC_index;
        std::vector <int> v_genB_index;
        std::vector <int> v_genGlu_index;
        
        std::vector <CLHEP::HepLorentzVector> v_genC_4mom;
        std::vector <CLHEP::HepLorentzVector> v_genB_4mom;
        std::vector <CLHEP::HepLorentzVector> v_genGlu_4mom;
        
        std::vector <int> v_genTop_index;
        std::vector <int> v_genTop_isHadronic;
        std::vector <CLHEP::HepLorentzVector> v_genTopVis_4mom;
        
        std::vector <std::vector <CLHEP::HepLorentzVector> > vv_genTop_consti_4mom;
        
        GenParticle *genHadTop = 0;
        
        GenParticle *genLepTop = 0;
        GenParticle *genLepTopB = 0;
        GenParticle *genWlep = 0;
        
        std::vector <CLHEP::HepLorentzVector> v_genLepTopB_4mom;
        std::vector <CLHEP::HepLorentzVector> v_genWlep_4mom;
        
        CLHEP::HepLorentzVector invisble_4mom_truth(0, 0, 0, 0);
        
        // GenParticles
        for(int iPart = 0; iPart < nParticle; iPart++)
        {
            GenParticle *genParticle = (GenParticle*) br_Particle->At(iPart);
            CLHEP::HepLorentzVector genParticle_4mom = delphesObjToHepLorentzVector(genParticle);
            
            int id = genParticle->PID;
            int status = genParticle->Status;
            
            
            //if(abs(id) == 1000006)
            //{
            //    printf("PdgId: 1000006, status = %d, m: %0.2f \n", status, genParticle_4mom.m());
            //}
            //
            //else if(abs(id) == 1000022)
            //{
            //    printf("PdgId: 1000022, status = %d, m: %0.2f \n", status, genParticle_4mom.m());
            //}
            
            // Mothers
            int mother1_index = genParticle->M1;
            int mother2_index = genParticle->M2;
            
            GenParticle *mother1 = 0;
            GenParticle *mother2 = 0;
            
            if(mother1_index >= 0)
            {
                mother1 = (GenParticle*) br_Particle->At(mother1_index);
            }
            
            if(mother2_index >= 0)
            {
                mother2 = (GenParticle*) br_Particle->At(mother2_index);
            }
            
            
            // Daughters
            int daughter1_index = genParticle->D1;
            int daughter2_index = genParticle->D2;
            
            GenParticle *daughter1 = 0;
            GenParticle *daughter2 = 0;
            
            if(daughter1_index >= 0)
            {
                daughter1 = (GenParticle*) br_Particle->At(daughter1_index);
            }
            
            if(daughter2_index >= 0)
            {
                daughter2 = (GenParticle*) br_Particle->At(daughter2_index);
            }
            
            
            // Gen c
            // Note: Must not be a charm coming from bottom
            if(abs(id) == 4)
            {
                //if(status == 22)
                if(
                    (!mother1 || (abs(mother1->PID) != 4 && abs(mother1->PID) != 5)) &&
                    (!mother2 || (abs(mother2->PID) != 4 && abs(mother2->PID) != 5))
                )
                {
                    GenParticle *genC = getFirstCopy(br_Particle, genParticle);
                    
                    if(genC->PT > _c_pTcut && fabs(genC->Eta) < _c_etaCut)
                    {
                        //int m1 = mother1? mother1->PID: 0;
                        //int m2 = mother2? mother2->PID: 0;
                        //
                        //int m1m1 = 0;
                        //int m1m2 = 0;
                        //
                        //int m2m1 = 0;
                        //int m2m2 = 0;
                        //
                        //if(m1)
                        //{
                        //    GenParticle *temp1 = (mother1->M1 >= 0)? getFirstCopy(br_Particle, (GenParticle*) br_Particle->At(mother1->M1)): (GenParticle*) 0;
                        //    GenParticle *temp2 = (mother1->M2 >= 0)? getFirstCopy(br_Particle, (GenParticle*) br_Particle->At(mother1->M2)): (GenParticle*) 0;
                        //    
                        //    m1m1 = temp1? temp1->PID: 0;
                        //    m1m2 = temp2? temp2->PID: 0;
                        //}
                        //
                        //if(m2)
                        //{
                        //    GenParticle *temp1 = (mother2->M1 >= 0)? getFirstCopy(br_Particle, (GenParticle*) br_Particle->At(mother2->M1)): (GenParticle*) 0;
                        //    GenParticle *temp2 = (mother2->M2 >= 0)? getFirstCopy(br_Particle, (GenParticle*) br_Particle->At(mother2->M2)): (GenParticle*) 0;
                        //    
                        //    m2m1 = temp1? temp1->PID: 0;
                        //    m2m2 = temp2? temp2->PID: 0;
                        //}
                        //
                        //printf(
                        //    "[%d/%d] "
                        //    "c quark: m1 %+d (%+d, %+d), m2 %+d (%+d, %+d), pT %0.3f, "
                        //    "\n",
                        //    iEvent+1, nEvent,
                        //    m1, m1m1, m1m2,
                        //    m2, m2m1, m2m2,
                        //    genC->PT
                        //);
                        
                        v_genC_index.push_back(iPart);
                        v_genC_4mom.push_back(delphesObjToHepLorentzVector(genC));
                        
                        outputInfo->c_n_truth += 1;
                        
                        outputInfo->v_c_pT_truth.push_back(genC->PT);
                        outputInfo->v_c_eta_truth.push_back(genC->Eta);
                        outputInfo->v_c_phi_truth.push_back(genC->Phi);
                        outputInfo->v_c_E_truth.push_back(genC->E);
                        outputInfo->v_c_px_truth.push_back(genC->Px);
                        outputInfo->v_c_py_truth.push_back(genC->Py);
                        outputInfo->v_c_pz_truth.push_back(genC->Pz);
                    }
                }
            }
            
            
            // Gen b
            if(abs(id) == 5)
            {
                //if(status == 22)
                if(
                    (!mother1 || abs(mother1->PID) != 5) &&
                    (!mother2 || abs(mother2->PID) != 5)
                )
                {
                    GenParticle *genB = getFirstCopy(br_Particle, genParticle);
                    
                    if(genB->PT > _b_pTcut && fabs(genB->Eta) < _b_etaCut)
                    {
                        v_genB_index.push_back(iPart);
                        v_genB_4mom.push_back(delphesObjToHepLorentzVector(genB));
                        
                        outputInfo->b_n_truth += 1;
                        
                        outputInfo->v_b_pT_truth.push_back(genB->PT);
                        outputInfo->v_b_eta_truth.push_back(genB->Eta);
                        outputInfo->v_b_phi_truth.push_back(genB->Phi);
                        outputInfo->v_b_E_truth.push_back(genB->E);
                        outputInfo->v_b_px_truth.push_back(genB->Px);
                        outputInfo->v_b_py_truth.push_back(genB->Py);
                        outputInfo->v_b_pz_truth.push_back(genB->Pz);
                    }
                }
            }
            
            
            // Gen top
            if(abs(id) == 6)
            {
                //printf("[%d/%d] Top: id %d, status %d \n", iEvent, nEvent, id, status);
                
                if(status == 22)
                {
                    GenParticle *genTop = getLastCopy(br_Particle, genParticle);
                    
                    CLHEP::HepLorentzVector genTop_4mom = delphesObjToHepLorentzVector(genTop);
                    
                    GenParticle *genW = selectDaughter(br_Particle, genTop, 24, true);
                    genW = getLastCopy(br_Particle, genW);
                    
                    GenParticle *genB = selectDaughter(br_Particle, genTop, 5, true);
                    
                    CLHEP::HepLorentzVector genB_4mom = delphesObjToHepLorentzVector(genB);
                    
                    bool isHadronic = isHadronicTop(br_Particle, genTop);
                    
                    if(genTop->PT > _t_pTcut && fabs(genTop->Eta) < _t_etaCut)
                    {
                        v_genTop_isHadronic.push_back(isHadronic);
                        v_genTop_index.push_back(iPart);
                        
                        if(isHadronic)
                        {
                            genHadTop = genTop;
                            
                            GenParticle *genWq1 = (GenParticle*) br_Particle->At(genW->D1);
                            GenParticle *genWq2 = (GenParticle*) br_Particle->At(genW->D2);
                            
                            GenParticle *temp;
                            
                            double Wq1b_m = (genWq1->P4() + genB->P4()).M();
                            double Wq2b_m = (genWq2->P4() + genB->P4()).M();
                            
                            if(Wq2b_m < Wq1b_m)
                            {
                                temp = genWq1;
                                genWq1 = genWq2;
                                genWq2 = temp;
                            }
                            
                            CLHEP::HepLorentzVector genWq1_4mom = delphesObjToHepLorentzVector(genWq1);
                            CLHEP::HepLorentzVector genWq2_4mom = delphesObjToHepLorentzVector(genWq2);
                            
                            //h1_genTop_pT->Fill(genParticle->PT);
                            
                            outputInfo->hadTop_n_truth++;
                            
                            outputInfo->v_hadTop_pT_truth.push_back(genTop->PT);
                            outputInfo->v_hadTop_eta_truth.push_back(genTop->Eta);
                            outputInfo->v_hadTop_phi_truth.push_back(genTop->Phi);
                            outputInfo->v_hadTop_m_truth.push_back(genTop->Mass);
                            outputInfo->v_hadTop_E_truth.push_back(genTop->E);
                            outputInfo->v_hadTop_px_truth.push_back(genTop->Px);
                            outputInfo->v_hadTop_py_truth.push_back(genTop->Py);
                            outputInfo->v_hadTop_pz_truth.push_back(genTop->Pz);
                            
                            outputInfo->v_hadTopB_pT_truth.push_back(genB->PT);
                            outputInfo->v_hadTopB_eta_truth.push_back(genB->Eta);
                            outputInfo->v_hadTopB_phi_truth.push_back(genB->Phi);
                            outputInfo->v_hadTopB_E_truth.push_back(genB->E);
                            outputInfo->v_hadTopB_px_truth.push_back(genB->Px);
                            outputInfo->v_hadTopB_py_truth.push_back(genB->Py);
                            outputInfo->v_hadTopB_pz_truth.push_back(genB->Pz);
                            outputInfo->v_hadTopB_Wq1deltaR_truth.push_back(getRapidityDeltaR(genB_4mom, genWq1_4mom));
                            outputInfo->v_hadTopB_Wq2deltaR_truth.push_back(getRapidityDeltaR(genB_4mom, genWq2_4mom));
                            outputInfo->v_hadTopB_hadTopDeltaR_truth.push_back(getRapidityDeltaR(genB_4mom, genTop_4mom));
                            
                            outputInfo->v_hadTopW_pT_truth.push_back(genW->PT);
                            outputInfo->v_hadTopW_eta_truth.push_back(genW->Eta);
                            outputInfo->v_hadTopW_phi_truth.push_back(genW->Phi);
                            outputInfo->v_hadTopW_E_truth.push_back(genW->E);
                            outputInfo->v_hadTopW_px_truth.push_back(genW->Px);
                            outputInfo->v_hadTopW_py_truth.push_back(genW->Py);
                            outputInfo->v_hadTopW_pz_truth.push_back(genW->Pz);
                            
                            
                            
                            outputInfo->v_Wq1_pT_truth.push_back(genWq1->PT);
                            outputInfo->v_Wq1_eta_truth.push_back(genWq1->Eta);
                            outputInfo->v_Wq1_phi_truth.push_back(genWq1->Phi);
                            outputInfo->v_Wq1_E_truth.push_back(genWq1->E);
                            outputInfo->v_Wq1_px_truth.push_back(genWq1->Px);
                            outputInfo->v_Wq1_py_truth.push_back(genWq1->Py);
                            outputInfo->v_Wq1_pz_truth.push_back(genWq1->Pz);
                            outputInfo->v_Wq1_pid_truth.push_back(genWq1->PID);
                            outputInfo->v_Wq1_Wq2deltaR_truth.push_back(getRapidityDeltaR(genWq1->P4(), genWq2->P4()));
                            outputInfo->v_Wq1_hadTopDeltaR_truth.push_back(getRapidityDeltaR(genTop_4mom, genWq1_4mom));
                            
                            outputInfo->v_Wq2_pT_truth.push_back(genWq2->PT);
                            outputInfo->v_Wq2_eta_truth.push_back(genWq2->Eta);
                            outputInfo->v_Wq2_phi_truth.push_back(genWq2->Phi);
                            outputInfo->v_Wq2_E_truth.push_back(genWq2->E);
                            outputInfo->v_Wq2_px_truth.push_back(genWq2->Px);
                            outputInfo->v_Wq2_py_truth.push_back(genWq2->Py);
                            outputInfo->v_Wq2_pz_truth.push_back(genWq2->Pz);
                            outputInfo->v_Wq2_pid_truth.push_back(genWq2->PID);
                            outputInfo->v_Wq2_hadTopDeltaR_truth.push_back(getRapidityDeltaR(genWq2_4mom, genTop_4mom));
                            
                            CLHEP::HepLorentzVector t_4mom_gen = delphesObjToHepLorentzVector(genTop);
                            CLHEP::HepLorentzVector Wq1_4mom_gen_boost = delphesObjToHepLorentzVector(genWq1);
                            
                            CLHEP::Hep3Vector boostVector = -t_4mom_gen.boostVector();
                            
                            Wq1_4mom_gen_boost.boost(boostVector);
                            
                            double cosThetaStar = t_4mom_gen.v().unit().dot(Wq1_4mom_gen_boost.v().unit());
                            
                            outputInfo->v_cosThetaStar_truth.push_back(cosThetaStar);
                            
                            std::pair <CLHEP::HepLorentzVector, CLHEP::HepLorentzVector> p_closestPair_4mom = getClosestPair(
                                {genB_4mom, genWq1_4mom, genWq2_4mom}
                            );
                            
                            double zk = max(p_closestPair_4mom.first.e(), p_closestPair_4mom.second.e()) / genTop->E;
                            double zb = genB->E / genTop->E;
                            
                            outputInfo->v_zk_truth.push_back(zk);
                            outputInfo->v_zb_truth.push_back(zb);
                            
                            
                            v_genTopVis_4mom.push_back(genTop_4mom);
                            
                            vv_genTop_consti_4mom.push_back({
                                genB_4mom,
                                genWq1_4mom,
                                genWq2_4mom
                            });
                        }
                        
                        else
                        {
                            genLepTop = genTop;
                            genLepTopB = genB;
                            
                            genWlep = (GenParticle*) br_Particle->At(genW->D1);
                            
                            // Select the other daughter if the current one isn't a lepton
                            if(abs(genWlep->PID) != 11 && abs(genWlep->PID) != 13 && abs(genWlep->PID) != 15)
                            {
                                genWlep = (GenParticle*) br_Particle->At(genW->D2);
                            }
                            
                            CLHEP::HepLorentzVector genWlep_4mom = delphesObjToHepLorentzVector(genWlep);
                            CLHEP::HepLorentzVector lepTopVis_4mom = genB_4mom + genWlep_4mom;
                            
                            v_genWlep_4mom.push_back(genWlep_4mom);
                            v_genLepTopB_4mom.push_back(genB_4mom);
                            
                            outputInfo->lepTop_n_truth++;
                            
                            outputInfo->v_lepTop_pT_truth.push_back(genTop->PT);
                            outputInfo->v_lepTop_eta_truth.push_back(genTop->Eta);
                            outputInfo->v_lepTop_phi_truth.push_back(genTop->Phi);
                            outputInfo->v_lepTop_m_truth.push_back(genTop->Mass);
                            outputInfo->v_lepTop_E_truth.push_back(genTop->E);
                            outputInfo->v_lepTop_px_truth.push_back(genTop->Px);
                            outputInfo->v_lepTop_py_truth.push_back(genTop->Py);
                            outputInfo->v_lepTop_pz_truth.push_back(genTop->Pz);
                            
                            outputInfo->v_lepTopB_pT_truth.push_back(genB->PT);
                            outputInfo->v_lepTopB_eta_truth.push_back(genB->Eta);
                            outputInfo->v_lepTopB_phi_truth.push_back(genB->Phi);
                            outputInfo->v_lepTopB_E_truth.push_back(genB->E);
                            outputInfo->v_lepTopB_px_truth.push_back(genB->Px);
                            outputInfo->v_lepTopB_py_truth.push_back(genB->Py);
                            outputInfo->v_lepTopB_pz_truth.push_back(genB->Pz);
                            outputInfo->v_lepTopB_lepTopDeltaR_truth.push_back(getRapidityDeltaR(genB_4mom, genTop_4mom));
                            outputInfo->v_lepTopB_lepTopVisDeltaR_truth.push_back(getRapidityDeltaR(genB_4mom, lepTopVis_4mom));
                            
                            outputInfo->v_lepTopW_pT_truth.push_back(genW->PT);
                            outputInfo->v_lepTopW_eta_truth.push_back(genW->Eta);
                            outputInfo->v_lepTopW_phi_truth.push_back(genW->Phi);
                            outputInfo->v_lepTopW_E_truth.push_back(genW->E);
                            outputInfo->v_lepTopW_px_truth.push_back(genW->Px);
                            outputInfo->v_lepTopW_py_truth.push_back(genW->Py);
                            outputInfo->v_lepTopW_pz_truth.push_back(genW->Pz);
                            
                            
                            outputInfo->v_Wlep_pT_truth.push_back(genWlep->PT);
                            outputInfo->v_Wlep_eta_truth.push_back(genWlep->Eta);
                            outputInfo->v_Wlep_phi_truth.push_back(genWlep->Phi);
                            outputInfo->v_Wlep_E_truth.push_back(genWlep->E);
                            outputInfo->v_Wlep_px_truth.push_back(genWlep->Px);
                            outputInfo->v_Wlep_py_truth.push_back(genWlep->Py);
                            outputInfo->v_Wlep_pz_truth.push_back(genWlep->Pz);
                            outputInfo->v_Wlep_pid_truth.push_back(genWlep->PID);
                            outputInfo->v_Wlep_lepTopDeltaR_truth.push_back(getRapidityDeltaR(genWlep_4mom, genTop_4mom));
                            outputInfo->v_Wlep_lepTopVisDeltaR_truth.push_back(getRapidityDeltaR(genWlep_4mom, lepTopVis_4mom));
                            
                            //double deltaRbl = genB->P4().DeltaR(genWlep->P4());
                            double deltaRbl = getRapidityDeltaR(genB->P4(), genWlep->P4());
                            double mbl = (genB->P4()+genWlep->P4()).M();
                            
                            outputInfo->v_lepTop_deltaRbl_truth.push_back(deltaRbl);
                            outputInfo->v_lepTop_mbl_truth.push_back(mbl);
                            
                            double zl = genWlep->E / (genB->E + genWlep->E);
                            
                            outputInfo->v_zl_truth.push_back(zl);
                            
                            
                            outputInfo->v_lepTopVis_pT_truth.push_back(lepTopVis_4mom.perp());
                            outputInfo->v_lepTopVis_eta_truth.push_back(lepTopVis_4mom.eta());
                            outputInfo->v_lepTopVis_phi_truth.push_back(lepTopVis_4mom.phi());
                            outputInfo->v_lepTopVis_m_truth.push_back(lepTopVis_4mom.m());
                            outputInfo->v_lepTopVis_E_truth.push_back(lepTopVis_4mom.e());
                            outputInfo->v_lepTopVis_px_truth.push_back(lepTopVis_4mom.px());
                            outputInfo->v_lepTopVis_py_truth.push_back(lepTopVis_4mom.py());
                            outputInfo->v_lepTopVis_pz_truth.push_back(lepTopVis_4mom.pz());
                            
                            
                            v_genTopVis_4mom.push_back(lepTopVis_4mom);
                            
                            vv_genTop_consti_4mom.push_back({
                                genB_4mom,
                                genWlep_4mom
                            });
                        }
                    }
                }
            }
            
            // Gen lepton from W
            if(abs(id) == 24 && daughter1 && daughter2)
            {
                //printf("[%d/%d] W: id %d, status %d, D1 %d, D2 %d \n", iEvent, nEvent, id, status, daughter1->PID, daughter2->PID);
                
                if(abs(daughter1->PID) == 11 || abs(daughter1->PID) == 13 || abs(daughter1->PID) == 15)
                {
                    v_genLepFromW_index.push_back(daughter1_index);
                }
                
                if(abs(daughter2->PID) == 11 || abs(daughter2->PID) == 13 || abs(daughter2->PID) == 15)
                {
                    v_genLepFromW_index.push_back(daughter2_index);
                }
            }
            
            // Gen MET
            if(status == 1 && (abs(id) == 12 || abs(id) == 14 || abs(id) == 16 || abs(id) == 1000022))
            {
                invisble_4mom_truth += genParticle_4mom;
            }
            
            
            if(id == +34 && status == 22)
            {
                nWprimePos++;
            }
            
            if(id == -34 && status == 22)
            {
                nWprimeNeg++;
            }
        }
        
        
        // EFlowTracks
        for(int iTrack = 0; iTrack < nTrack; iTrack++)
        {
            Track *track = (Track*) br_EFlowTrack->At(iTrack);
            
            GenParticle *track_genPart = (GenParticle*) track->Particle.GetObject();
            
            //printf(
            //    "[%d/%d] "
            //    "EFlowTrack %d/%d: PID %+d (%+d) "
            //    "\n",
            //    iEvent+1, nEvent,
            //    iTrack+1, nTrack,
            //    track->PID, track_genPart->PID
            //);
            
            fastjet::PseudoJet fj_pseudoJet(
                track->P4().Px(),
                track->P4().Py(),
                track->P4().Pz(),
                track->P4().E()
            );
            
            fj_pseudoJet.set_user_index((int) _DELPHES_RECOID::_DELPHES_RECOID_TRACK);
            
            fj_input.push_back(fj_pseudoJet);
        }
        
        
        // EFlowPhotons
        for(int iPhoton = 0; iPhoton < nPhoton; iPhoton++)
        {
            Photon *photon = (Photon*) br_EFlowPhoton->At(iPhoton);
            
            //printf(
            //    "[%d/%d] "
            //    "EFlowPhoton %d/%d: PID %d "
            //    "\n",
            //    iEvent+1, nEvent,
            //    iPhoton+1, nPhoton,
            //    photon->PID
            //);
            
            fastjet::PseudoJet fj_pseudoJet(
                photon->P4().Px(),
                photon->P4().Py(),
                photon->P4().Pz(),
                photon->P4().E()
            );
            
            fj_pseudoJet.set_user_index((int) _DELPHES_RECOID::_DELPHES_RECOID_PHOTON);
            
            fj_input.push_back(fj_pseudoJet);
        }
        
        
        // EFlowNeutralHadrons
        for(int iNeutralHad = 0; iNeutralHad < nNeutralHad; iNeutralHad++)
        {
            Tower *neutralHad = (Tower*) br_EFlowNeutralHadron->At(iNeutralHad);
            
            //printf(
            //    "[%d/%d] "
            //    "EFlowNeutralHadron %d/%d: PID %d "
            //    "\n",
            //    iEvent+1, nEvent,
            //    iNeutralHad+1, nNeutralHad,
            //    neutralHad->PID
            //);
            
            fastjet::PseudoJet fj_pseudoJet(
                neutralHad->P4().Px(),
                neutralHad->P4().Py(),
                neutralHad->P4().Pz(),
                neutralHad->P4().E()
            );
            
            fj_pseudoJet.set_user_index((int) _DELPHES_RECOID::_DELPHES_RECOID_NEUTRALHADRON);
            
            fj_input.push_back(fj_pseudoJet);
        }
        
        
        // Input to fastjet cannot be empty
        if(!fj_input.size())
        {
            continue;
        }
        
        
        // Reco jet
        std::vector <fastjet::PseudoJet> fj_inclusiveJets;
        std::vector <fastjet::PseudoJet> fj_sortedJets;
        
        fastjet::ClusterSequence fj_jet_clustSeq(fj_input, *fj_jetDef);
        
        fj_inclusiveJets = fj_jet_clustSeq.inclusive_jets(_jet_pTcut);
        fj_sortedJets = sorted_by_pt(fj_inclusiveJets);
        
        std::vector <CLHEP::HepLorentzVector> v_jet_4mom_reco;
        
        int nJet = fj_sortedJets.size();
        
        for(int iJet = 0; iJet < nJet; iJet++)
        {
            fastjet::PseudoJet fj_pseudoJet = fj_sortedJets.at(iJet);
            
            if(fj_pseudoJet.perp() < _jet_pTcut || fabs(fj_pseudoJet.eta()) > _jet_etaCut)
            {
                continue;
            }
            
            CLHEP::HepLorentzVector jet_4mom_reco = PseudoJetToHepLorentzVector(fj_pseudoJet);
            
            v_jet_4mom_reco.push_back(jet_4mom_reco);
        }
        
        // Jet b-parton matching
        std::vector <double> v_jetB_deltaR_min;
        
        if(v_genB_index.size())
        {
            TMatrixD mat_temp;
            
            v_jetB_deltaR_min = getMinDeltaR(
                v_jet_4mom_reco,
                v_genB_4mom,
                mat_temp,
                true
            );
        }
        
        
        // Subjet c-parton matching
        std::vector <double> v_jetC_deltaR_min;
        
        if(v_genC_index.size())
        {
            TMatrixD mat_temp;
            
            v_jetC_deltaR_min = getMinDeltaR(
                v_jet_4mom_reco,
                v_genC_4mom,
                mat_temp,
                true
            );
        }
        
        
        // B-tagging parametrization
        std::vector <bool> v_jet_isBtagged_reco;
        std::vector <CLHEP::HepLorentzVector> v_jet_bTagged_4mom_reco;
        
        for(int iJet = 0; iJet < v_jet_4mom_reco.size(); iJet++)
        {
            int jet_pid = 0;
            
            if(v_jetB_deltaR_min.size() && v_jetB_deltaR_min.at(iJet) < _jetR)
            {
                jet_pid = 5;
            }
            
            else if(v_jetC_deltaR_min.size() && v_jetC_deltaR_min.at(iJet) < _jetR)
            {
                jet_pid = 4;
            }
            
            bool isBtagged = isBtagged_parametrized(v_jet_4mom_reco.at(iJet), jet_pid);
            
            //nJetBtagged += (int) isBtagged;
            
            v_jet_isBtagged_reco.push_back(isBtagged);
            
            if(isBtagged)
            {
                v_jet_bTagged_4mom_reco.push_back(v_jet_4mom_reco.at(iJet));
            }
        }
        
        
        // Reco fat jet
        std::vector <fastjet::PseudoJet> fj_inclusiveFatJets;
        std::vector <fastjet::PseudoJet> fj_sortedFatJets;
        
        fastjet::ClusterSequence fj_fatJet_clustSeq(fj_input, *fj_fatJetDef);
        
        fj_inclusiveFatJets = fj_fatJet_clustSeq.inclusive_jets(_t_pTcut);
        fj_sortedFatJets = sorted_by_pt(fj_inclusiveFatJets);
        
        
        CLHEP::HepLorentzVector hepTop1_4mom_reco(0, 0, 0, 0);
        
        int nFatJet = fj_sortedFatJets.size();
        
        for(int iFatJet = 0; iFatJet < nFatJet; iFatJet++)
        {
            fastjet::PseudoJet fj_fatJet = fj_sortedFatJets.at(iFatJet);
            
            if(fj_fatJet.perp() < _t_pTcut || fabs(fj_fatJet.eta()) > _t_etaCut)
            {
                continue;
            }
            
            // Soft-drop
            // Large R (>> R of the jet), so that the all the constituents are clustered
            //fastjet::JetDefinition *fj_softDropCAdef = new fastjet::JetDefinition(fastjet::cambridge_algorithm, 1000, fj_recombScheme, fj_strategy);
            //
            //fastjet::ClusterSequence fj_softDrop_clustSeq(fj_fatJet.constituents(), *fj_softDropCAdef);
            //
            //std::vector <fastjet::PseudoJet> fj_softDrop_inclJets = fj_softDrop_clustSeq.inclusive_jets(0);
            //std::vector <fastjet::PseudoJet> fj_softDrop_sortedJets = sorted_by_pt(fj_softDrop_inclJets);
            
            fastjet::PseudoJet fj_fatJet_softDrop = fj_fatJet;
            
            if(applySD)
            {
                double sd_z_cut = 0.1;
                double sd_beta  = 0.0;
                double sd_R0    = 1.0; // 1.0 is the default value
                fastjet::contrib::SoftDrop fj_softDrop(sd_beta, sd_z_cut, sd_R0);
                
                //fastjet::PseudoJet fj_fatJet_softDrop = fj_softDrop(fj_softDrop_sortedJets.at(0));
                fj_fatJet_softDrop = fj_softDrop(fj_fatJet);
                
                //printf(
                //    "[%d/%d] "
                //    "Fat jet %d/%d: "
                //    "(SD-pT)/pT = %0.4f/%0.4f = %0.4f, "
                //    "(SD-m)/m = %0.4f/%0.4f = %0.4f, "
                //    "\n",
                //    
                //    iEvent+1, nEvent,
                //    iFatJet+1, nFatJet,
                //    fj_fatJet_softDrop.pt(), fj_fatJet.pt(), fj_fatJet_softDrop.pt()/fj_fatJet.pt(),
                //    fj_fatJet_softDrop.m(), fj_fatJet.m(), fj_fatJet_softDrop.m()/fj_fatJet.m()
                //);
            }
            
            
            fastjet::PseudoJet fj_fatJet_raw = fj_fatJet;
            fj_fatJet = fj_fatJet_softDrop;
            
            
            // Re-check pT and eta after soft-drop
            if(fj_fatJet.perp() < _t_pTcut || fabs(fj_fatJet.eta()) > _t_etaCut)
            {
                continue;
            }
            
            outputInfo->v_hepTop_raw_pT_reco.push_back(fj_fatJet_raw.perp());
            outputInfo->v_hepTop_raw_eta_reco.push_back(fj_fatJet_raw.eta());
            outputInfo->v_hepTop_raw_phi_reco.push_back(fj_fatJet_raw.phi());
            outputInfo->v_hepTop_raw_E_reco.push_back(fj_fatJet_raw.e());
            outputInfo->v_hepTop_raw_px_reco.push_back(fj_fatJet_raw.px());
            outputInfo->v_hepTop_raw_py_reco.push_back(fj_fatJet_raw.py());
            outputInfo->v_hepTop_raw_pz_reco.push_back(fj_fatJet_raw.pz());
            outputInfo->v_hepTop_raw_m_reco.push_back(fj_fatJet_raw.m());
            
            
            CLHEP::HepLorentzVector fatJet_4mom_reco = PseudoJetToHepLorentzVector(fj_fatJet);
            
            HEPTopTagger::HEPTopTagger tagger(fj_fatJet);
            HEPTopTagger::HEPTopTagger tagger_default(fj_fatJet);
            HEPTopTagger::HEPTopTagger tagger_dummy(fj_fatJet);
            
            // Unclustering, Filtering & Subjet Settings
            tagger.set_max_subjet_mass(30);
            tagger.set_mass_drop_threshold(0.8);
            tagger.set_filtering_R(0.3);
            tagger.set_filtering_n(5);
            tagger.set_filtering_minpt_subjet(30);
            
            tagger_default.set_max_subjet_mass(30);
            tagger_default.set_mass_drop_threshold(0.8);
            tagger_default.set_filtering_R(0.3);
            tagger_default.set_filtering_n(5);
            tagger_default.set_filtering_minpt_subjet(30);
            
            // How to select among candidates
            tagger.set_mode(HEPTopTagger::TWO_STEP_FILTER);
            
            tagger_default.set_mode(HEPTopTagger::TWO_STEP_FILTER);
            
            // Requirements to accept a candidate
            tagger.set_top_minpt(_t_pTcut); 
            tagger.set_top_mass_range(0, 9999); 
            tagger.set_fw(1);
            
            tagger_default.set_top_minpt(_t_pTcut); 
            tagger_default.set_top_mass_range(150, 200); 
            tagger_default.set_fw(0.15);
            
            // Run the tagger
            tagger.run();
            
            //tagger_default.run();
            
            
            //if(!tagger.is_maybe_top())
            //{
            //    continue;
            //}
            
            
            outputInfo->hepTop_n_reco += 1;
            
            outputInfo->v_hepTop_pT_reco.push_back(fatJet_4mom_reco.perp());
            outputInfo->v_hepTop_eta_reco.push_back(fatJet_4mom_reco.eta());
            outputInfo->v_hepTop_phi_reco.push_back(fatJet_4mom_reco.phi());
            outputInfo->v_hepTop_E_reco.push_back(fatJet_4mom_reco.e());
            outputInfo->v_hepTop_px_reco.push_back(fatJet_4mom_reco.px());
            outputInfo->v_hepTop_py_reco.push_back(fatJet_4mom_reco.py());
            outputInfo->v_hepTop_pz_reco.push_back(fatJet_4mom_reco.pz());
            outputInfo->v_hepTop_m_reco.push_back(fatJet_4mom_reco.m());
            
            
            double genTop_deltaR_min = 9999;
            double genHadTop_deltaR_min = 9999;
            double genLepTop_deltaR_min = 9999;
            
            int nearestGenTop_index = -1;
            int nearestGenHadTop_index = -1;
            int nearestGenLepTop_index = -1;
            
            bool isHadTop = false;
            
            int iGenHadTop = 0;
            int iGenLepTop = 0;
            
            for(int iGenTop = 0; iGenTop < v_genTop_index.size(); iGenTop++)
            {
                //GenParticle *genTop = (GenParticle*) br_Particle->At(v_genTop_index.at(iGenTop));
                
                //if(!v_genTop_isHadronic.at(iGenTop))
                //{
                //    continue;
                //}
                
                CLHEP::HepLorentzVector t_4mom_gen = v_genTopVis_4mom.at(iGenTop);
                //t_4mom_gen.setT(genTop->E);
                //t_4mom_gen.setX(genTop->Px);
                //t_4mom_gen.setY(genTop->Py);
                //t_4mom_gen.setZ(genTop->Pz);
                
                //double deltaR = fatJet_4mom_reco.deltaR(t_4mom_gen);
                double deltaR = getRapidityDeltaR(fatJet_4mom_reco, t_4mom_gen);
                
                if(v_genTop_isHadronic.at(iGenTop) && deltaR < genHadTop_deltaR_min)
                {
                    genHadTop_deltaR_min = deltaR;
                    
                    nearestGenHadTop_index = iGenHadTop;
                }
                
                else if(!v_genTop_isHadronic.at(iGenTop) && deltaR < genLepTop_deltaR_min)
                {
                    genLepTop_deltaR_min = deltaR;
                    
                    nearestGenLepTop_index = iGenLepTop;
                }
                
                
                //if(deltaR < genTop_deltaR_min)
                //{
                //    genTop_deltaR_min = deltaR;
                //    
                //    nearestGenTop_index = iGenTop;
                //}
                
                
                // Update the had-top and lep-top indices
                if(v_genTop_isHadronic.at(iGenTop))
                {
                    iGenHadTop++;
                }
                
                else
                {
                    iGenLepTop++;
                }
            }
            
            
            if(v_genTopVis_4mom.size())
            {
                TMatrixD mat_genTopMatch;
                
                std::vector <double> v_genTop_deltaR = getMinDeltaR(
                    v_genTopVis_4mom,
                    {fatJet_4mom_reco},
                    mat_genTopMatch,
                    true
                );
                
                nearestGenTop_index = std::distance(
                    v_genTop_deltaR.begin(),
                    std::min_element(v_genTop_deltaR.begin(), v_genTop_deltaR.end())
                );
                
                genTop_deltaR_min = v_genTop_deltaR.at(nearestGenTop_index);
            }
            
            
            // Count the number of gen-constituents in the reco jet
            int nGenTopConstiMatched = 0;
            
            if(nearestGenTop_index >= 0)
            {
                std::vector <CLHEP::HepLorentzVector> v_genTop_consti_4mom = vv_genTop_consti_4mom.at(nearestGenTop_index);
                
                for(int iGenTopConsti = 0; iGenTopConsti < v_genTop_consti_4mom.size(); iGenTopConsti++)
                {
                    double deltaR = getRapidityDeltaR(v_genTop_consti_4mom.at(iGenTopConsti), fatJet_4mom_reco);
                    
                    nGenTopConstiMatched += (deltaR < _fatJetR);
                }
            }
            
            
            outputInfo->v_hepTop_nearestGenHadTop_index.push_back(nearestGenHadTop_index);
            outputInfo->v_hepTop_nearestGenLepTop_index.push_back(nearestGenLepTop_index);
            
            outputInfo->v_hepTop_genHadTop_deltaR_reco.push_back(genHadTop_deltaR_min);
            outputInfo->v_hepTop_genLepTop_deltaR_reco.push_back(genLepTop_deltaR_min);
            
            outputInfo->v_hepTop_nGenTopConstiMatched_reco.push_back(nGenTopConstiMatched);
            
            outputInfo->v_hepTop_isMayBeTop_reco.push_back(tagger.is_maybe_top());
            outputInfo->v_hepTop_isTagged_reco.push_back(tagger_default.is_tagged());
            
            jet_nMayBeTop += (int) tagger.is_maybe_top();
            jet_nTopTagged += (int) tagger_default.is_tagged();
            
            
            // Jet image
            fastjet::PseudoJet pseudojet_image = fj_fatJet;
            //fastjet::PseudoJet pseudojet_image = fj_fatJet_softDrop;
            
            
            // Cluster into exactly jets
            // If there are fewer than 3, returns the constituents
            fastjet::ClusterSequence fj_fatJetExcSubJet_clustSeq(pseudojet_image.constituents(), *fj_fatJetExcSubJetDef);
            std::vector <fastjet::PseudoJet> fj_fatJetExcSubJets = fj_fatJetExcSubJet_clustSeq.exclusive_jets_up_to(3);
            fj_fatJetExcSubJets = sorted_by_E(fj_fatJetExcSubJets);
            
            CLHEP::HepLorentzVector hepTop_4mom = PseudoJetToHepLorentzVector(pseudojet_image);
            
            int nConsti = pseudojet_image.constituents().size();
            int nFatJetExcSubJet = fj_fatJetExcSubJets.size();
            
            // If not is_maybe_top, then use the 3 exclusive subjets
            if(!tagger.is_maybe_top() && nFatJetExcSubJet >= 3)
            {
                tagger._HEPTopTagger_opt._top_candidate = fj_fatJet;
                tagger._HEPTopTagger_opt._top_subs = sorted_by_pt(fj_fatJetExcSubJets);
                tagger._HEPTopTagger_opt.store_topsubjets(fj_fatJetExcSubJets);
            }
            
            // Dummy tagger for subjets
            if(nFatJetExcSubJet >= 3)
            {
                tagger_dummy._HEPTopTagger_opt._top_candidate = fj_fatJet;
                tagger_dummy._HEPTopTagger_opt._top_subs = sorted_by_pt(fj_fatJetExcSubJets);
                tagger_dummy._HEPTopTagger_opt.store_topsubjets(fj_fatJetExcSubJets);
            }
            
            double subJet12_m = _defaultVal;
            double subJet23_m = _defaultVal;
            double subJet31_m = _defaultVal;
            
            double subJet123_m = _defaultVal;
            
            double frec12 = _defaultVal;
            double frec23 = _defaultVal;
            double frec31 = _defaultVal;
            
            double frec = _defaultVal;
            
            double zk = _defaultVal;
            double zb = _defaultVal;
            double cosThetaStar = _defaultVal;
            
            int nSubJetBtagged = 0;
            int nSubJetBmatched = 0;
            
            double subJet1B_deltaR_min = _defaultVal1;
            double subJet2B_deltaR_min = _defaultVal1;
            double subJet3B_deltaR_min = _defaultVal1;
            
            double subJet1C_deltaR_min = _defaultVal1;
            double subJet2C_deltaR_min = _defaultVal1;
            double subJet3C_deltaR_min = _defaultVal1;
            
            std::vector <CLHEP::HepLorentzVector> v_subJet_4mom;
            
            CLHEP::HepLorentzVector t_4mom_reco;
            CLHEP::HepLorentzVector b_4mom_reco;
            CLHEP::HepLorentzVector Wj1_4mom_reco;
            CLHEP::HepLorentzVector Wj2_4mom_reco;
            
            //if(tagger.is_maybe_top() || nFatJetExcSubJet >= 3)
            if(nFatJetExcSubJet >= 3)
            {
                t_4mom_reco = PseudoJetToHepLorentzVector(tagger_dummy.t());
                b_4mom_reco = PseudoJetToHepLorentzVector(tagger_dummy.b());
                Wj1_4mom_reco = PseudoJetToHepLorentzVector(tagger_dummy.W1());
                Wj2_4mom_reco = PseudoJetToHepLorentzVector(tagger_dummy.W2());
                
                
                // Subjet variables
                CLHEP::HepLorentzVector subJet1_4mom_reco = PseudoJetToHepLorentzVector(tagger_dummy.j1());
                CLHEP::HepLorentzVector subJet2_4mom_reco = PseudoJetToHepLorentzVector(tagger_dummy.j2());
                CLHEP::HepLorentzVector subJet3_4mom_reco = PseudoJetToHepLorentzVector(tagger_dummy.j3());
                
                v_subJet_4mom.push_back(subJet1_4mom_reco);
                v_subJet_4mom.push_back(subJet2_4mom_reco);
                v_subJet_4mom.push_back(subJet3_4mom_reco);
                
                int nSubJet = v_subJet_4mom.size();
                
                subJet12_m = (subJet1_4mom_reco + subJet2_4mom_reco).m();
                subJet23_m = (subJet2_4mom_reco + subJet3_4mom_reco).m();
                subJet31_m = (subJet3_4mom_reco + subJet1_4mom_reco).m();
                
                subJet123_m = (subJet1_4mom_reco + subJet2_4mom_reco + subJet3_4mom_reco).m();
                
                frec12 = fabs(subJet12_m/subJet123_m/_WbyTop_mRatio - 1);
                frec23 = fabs(subJet23_m/subJet123_m/_WbyTop_mRatio - 1);
                frec31 = fabs(subJet31_m/subJet123_m/_WbyTop_mRatio - 1);
                
                frec = std::min(std::min(frec12, frec23), frec31);
                
                
                // Polarization variables
                CLHEP::HepLorentzVector t_4mom_reco = PseudoJetToHepLorentzVector(tagger_dummy.t());
                CLHEP::HepLorentzVector b_4mom_reco = PseudoJetToHepLorentzVector(tagger_dummy.b());
                
                CLHEP::HepLorentzVector Wj1_4mom_reco = PseudoJetToHepLorentzVector(tagger_dummy.W1());
                CLHEP::HepLorentzVector Wj2_4mom_reco = PseudoJetToHepLorentzVector(tagger_dummy.W2());
                
                CLHEP::Hep3Vector boostVector = -t_4mom_reco.boostVector();
                
                if((b_4mom_reco+Wj2_4mom_reco).m() < (b_4mom_reco+Wj1_4mom_reco).m())
                {
                    CLHEP::HepLorentzVector temp = Wj1_4mom_reco;
                    Wj1_4mom_reco = Wj2_4mom_reco;
                    Wj2_4mom_reco = temp;
                }
                
                CLHEP::HepLorentzVector Wj1_4mom_reco_boost = Wj1_4mom_reco;
                
                Wj1_4mom_reco_boost.boost(boostVector);
                
                std::pair <CLHEP::HepLorentzVector, CLHEP::HepLorentzVector> p_closestPair_4mom = getClosestPair(
                    {b_4mom_reco, Wj1_4mom_reco, Wj2_4mom_reco}
                );
                
                zk = max(p_closestPair_4mom.first.e(), p_closestPair_4mom.second.e()) / t_4mom_reco.e();
                zb = b_4mom_reco.e() / t_4mom_reco.e();
                
                cosThetaStar = t_4mom_reco.v().unit().dot(Wj1_4mom_reco_boost.v().unit());
                
                
                // Subjet b-parton matching
                std::vector <double> v_subJetB_deltaR_min;
                
                if(v_genB_index.size())
                {
                    TMatrixD mat_temp;
                    
                    v_subJetB_deltaR_min = getMinDeltaR(
                        v_subJet_4mom,
                        v_genB_4mom,
                        mat_temp,
                        true
                    );
                    
                    subJet1B_deltaR_min = v_subJetB_deltaR_min.at(0);
                    subJet2B_deltaR_min = v_subJetB_deltaR_min.at(1);
                    subJet3B_deltaR_min = v_subJetB_deltaR_min.at(2);
                }
                
                
                // Subjet c-parton matching
                std::vector <double> v_subJetC_deltaR_min;
                
                if(v_genC_index.size())
                {
                    TMatrixD mat_temp;
                    
                    v_subJetC_deltaR_min = getMinDeltaR(
                        v_subJet_4mom,
                        v_genC_4mom,
                        mat_temp,
                        true
                    );
                    
                    subJet1C_deltaR_min = v_subJetC_deltaR_min.at(0);
                    subJet2C_deltaR_min = v_subJetC_deltaR_min.at(1);
                    subJet3C_deltaR_min = v_subJetC_deltaR_min.at(2);
                }
                
                
                // B-tagging parametrization
                for(int iSubJet = 0; iSubJet < nSubJet; iSubJet++)
                {
                    int subJet_pid = 0;
                    
                    if(v_subJetB_deltaR_min.size() && v_subJetB_deltaR_min.at(iSubJet) < _fatJetRby2)
                    {
                        subJet_pid = 5;
                    }
                    
                    else if(v_subJetC_deltaR_min.size() && v_subJetC_deltaR_min.at(iSubJet) < _fatJetRby2)
                    {
                        subJet_pid = 4;
                    }
                    
                    bool isBtagged = isBtagged_parametrized(v_subJet_4mom.at(iSubJet), subJet_pid);
                    
                    nSubJetBtagged += (int) isBtagged;
                }
            }
            
            
            //
            nSubJetBmatched = (subJet1B_deltaR_min < _fatJetRby2) + (subJet2B_deltaR_min < _fatJetRby2) + (subJet3B_deltaR_min < _fatJetRby2);
            
            outputInfo->v_hepTop_nSubJetBtagged_reco.push_back(nSubJetBtagged);
            outputInfo->v_hepTop_nSubJetBmatched_reco.push_back(nSubJetBmatched);
            outputInfo->v_hepTop_subJet1B_deltaR_reco.push_back(subJet1B_deltaR_min);
            outputInfo->v_hepTop_subJet2B_deltaR_reco.push_back(subJet2B_deltaR_min);
            outputInfo->v_hepTop_subJet3B_deltaR_reco.push_back(subJet3B_deltaR_min);
            
            
            // b-quarks in fatjet
            TMatrixD mat_fatJetB_deltaR;
            
            std::vector <double> v_fatJetB_deltaR = getMinDeltaR(
                {fatJet_4mom_reco},
                v_genB_4mom,
                mat_fatJetB_deltaR,
                true
            );
            
            int nBinFatJet = 0;
            
            for(int iB = 0; iB < mat_fatJetB_deltaR.GetNcols(); iB++)
            {
                if(mat_fatJetB_deltaR(0, iB) < _fatJetR)
                {
                    nBinFatJet++;
                }
            }
            
            outputInfo->v_hepTop_nBinFatJet_reco.push_back(nBinFatJet);
            
            
            // b-jets in fatjet
            TMatrixD mat_fatJetBtaggedJet_deltaR;
            
            std::vector <double> v_fatJetBtaggedJet_deltaR = getMinDeltaR(
                {fatJet_4mom_reco},
                v_jet_bTagged_4mom_reco,
                mat_fatJetBtaggedJet_deltaR,
                true
            );
            
            int nBtaggedJetInFatJet = 0;
            
            for(int iBtaggedJet = 0; iBtaggedJet < mat_fatJetBtaggedJet_deltaR.GetNcols(); iBtaggedJet++)
            {
                if(mat_fatJetBtaggedJet_deltaR(0, iBtaggedJet) < _fatJetR)
                {
                    nBtaggedJetInFatJet++;
                }
            }
            
            outputInfo->v_hepTop_nBtaggedJetInFatJet_reco.push_back(nBtaggedJetInFatJet);
            
            
            //
            outputInfo->v_hepTop_nExcSubJet_reco.push_back(nFatJetExcSubJet);
            
            outputInfo->v_hepTop_subJet12_m_reco.push_back(subJet12_m);
            outputInfo->v_hepTop_subJet23_m_reco.push_back(subJet23_m);
            outputInfo->v_hepTop_subJet31_m_reco.push_back(subJet31_m);
            
            outputInfo->v_hepTop_subJet123_m_reco.push_back(subJet123_m);
            
            outputInfo->v_hepTop_frec_reco.push_back(frec);
            
            outputInfo->v_hepTop_zk_reco.push_back(zk);
            outputInfo->v_hepTop_zb_reco.push_back(zb);
            outputInfo->v_hepTop_cosThetaStar_reco.push_back(cosThetaStar);
            
            
            // For leptonic top
            fastjet::ClusterSequence fj_fatJetExcSubJet_clustSeq_lep(fj_fatJet.constituents(), *fj_fatJetExcSubJetDef);
            std::vector <fastjet::PseudoJet> fj_fatJetExcSubJets_lep = fj_fatJetExcSubJet_clustSeq_lep.exclusive_jets_up_to(2);
            fj_fatJetExcSubJets_lep = sorted_by_pt(fj_fatJetExcSubJets_lep);
            
            double zl = -9;
            
            double subJetLep_genLep_deltaR = 999;
            double subJetLep_genB_deltaR = 999;
            
            double subJetB_genB_deltaR = 999;
            double subJetB_genLep_deltaR = 999;
            
            double subJet1_miniIso = 999;
            double subJet2_miniIso = 999;
            
            if(fj_fatJetExcSubJets_lep.size() == 2)
            {
                std::vector <fastjet::PseudoJet> v_subJet1_consti = fj_fatJetExcSubJets_lep.at(0).constituents();
                v_subJet1_consti = sorted_by_pt(v_subJet1_consti);
                
                std::vector <fastjet::PseudoJet> v_subJet2_consti = fj_fatJetExcSubJets_lep.at(1).constituents();
                v_subJet2_consti = sorted_by_pt(v_subJet2_consti);
                
                fastjet::PseudoJet pseudoJet_subJet1_trk1(0, 0, 0, 0);
                fastjet::PseudoJet pseudoJet_subJet2_trk1(0, 0, 0, 0);
                
                for(int iConsti = 0; iConsti < (int) v_subJet1_consti.size(); iConsti++)
                {
                    if(v_subJet1_consti.at(iConsti).user_index() == (int) _DELPHES_RECOID::_DELPHES_RECOID_TRACK)
                    {
                        pseudoJet_subJet1_trk1 = v_subJet1_consti.at(iConsti);
                        break;
                    }
                }
                
                for(int iConsti = 0; iConsti < (int) v_subJet2_consti.size(); iConsti++)
                {
                    if(v_subJet2_consti.at(iConsti).user_index() == (int) _DELPHES_RECOID::_DELPHES_RECOID_TRACK)
                    {
                        pseudoJet_subJet2_trk1 = v_subJet2_consti.at(iConsti);
                        break;
                    }
                }
                
                if(pseudoJet_subJet1_trk1.perp())
                {
                    subJet1_miniIso = getFastJetMiniIso(
                        //fj_fatJetExcSubJets_lep.at(0),
                        //fj_fatJet.constituents()
                        
                        pseudoJet_subJet1_trk1,
                        fj_fatJet.constituents()
                    );
                }
                
                if(pseudoJet_subJet2_trk1.perp())
                {
                    subJet2_miniIso = getFastJetMiniIso(
                        //fj_fatJetExcSubJets_lep.at(1),
                        //fj_fatJet.constituents()
                        
                        pseudoJet_subJet2_trk1,
                        fj_fatJet.constituents()
                    );
                }
                
                //fastjet::PseudoJet pseudojet_lep = fj_fatJetExcSubJets_lep.at(0);
                //fastjet::PseudoJet pseudojet_b = fj_fatJetExcSubJets_lep.at(1);
                
                fastjet::PseudoJet pseudojet_lep = pseudoJet_subJet1_trk1;
                fastjet::PseudoJet pseudojet_b = fj_fatJetExcSubJets_lep.at(1);
                
                if(subJet2_miniIso < subJet1_miniIso)
                {
                    pseudojet_lep = pseudoJet_subJet2_trk1;
                    pseudojet_b = fj_fatJetExcSubJets_lep.at(0);
                }
                
                zl = pseudojet_lep.e() / fj_fatJet.e();
                
                CLHEP::HepLorentzVector subJetLep_4mom = PseudoJetToHepLorentzVector(pseudojet_lep);
                CLHEP::HepLorentzVector subJetB_4mom = PseudoJetToHepLorentzVector(pseudojet_b);
                
                // Reco-lep, gen-lep
                if(pseudojet_lep.perp() && v_genWlep_4mom.size())
                {
                    TMatrixD mat_temp;
                    
                    subJetLep_genLep_deltaR = getMinDeltaR(
                        {subJetLep_4mom},
                        v_genWlep_4mom,
                        mat_temp,
                        true
                    ).at(0);
                }
                
                // Reco-lep, gen-b
                if(pseudojet_lep.perp() && v_genLepTopB_4mom.size())
                {
                    TMatrixD mat_temp;
                    
                    subJetLep_genB_deltaR = getMinDeltaR(
                        {subJetLep_4mom},
                        v_genLepTopB_4mom,
                        mat_temp,
                        true
                    ).at(0);
                }
                
                // Reco-b, gen-b
                if(pseudojet_b.perp() && v_genLepTopB_4mom.size())
                {
                    TMatrixD mat_temp;
                    
                    subJetB_genB_deltaR = getMinDeltaR(
                        {subJetB_4mom},
                        v_genLepTopB_4mom,
                        mat_temp,
                        true
                    ).at(0);
                }
                
                // Reco-b, gen-lep
                if(pseudojet_b.perp() && v_genWlep_4mom.size())
                {
                    TMatrixD mat_temp;
                    
                    subJetB_genLep_deltaR = getMinDeltaR(
                        {subJetB_4mom},
                        v_genWlep_4mom,
                        mat_temp,
                        true
                    ).at(0);
                }
            }
            
            outputInfo->v_hepTop_zl_reco.push_back(zl);
            
            outputInfo->v_hepTop_lep_subJetLep_genLep_deltaR_reco.push_back(subJetLep_genLep_deltaR);
            outputInfo->v_hepTop_lep_subJetLep_genB_deltaR_reco.push_back(subJetLep_genB_deltaR);
            
            outputInfo->v_hepTop_lep_subJetB_genB_deltaR_reco.push_back(subJetB_genB_deltaR);
            outputInfo->v_hepTop_lep_subJetB_genLep_deltaR_reco.push_back(subJetB_genLep_deltaR);
            
            outputInfo->v_hepTop_lepSubJet1_miniIso_reco.push_back(subJet1_miniIso);
            outputInfo->v_hepTop_lepSubJet2_miniIso_reco.push_back(subJet2_miniIso);
            
            
            
            fastjet::PseudoJet pseudojet_subStruc = fj_fatJet;
            
            // N-subjettiness
            double tauNm1 = 1;
            
            for(int iTauN = 0; iTauN <= _hepTop_tauN_max; iTauN++)
            {
                double tauN = 1;
                double tauNratio = 0;
                
                if(iTauN)
                {
                    fastjet::contrib::Nsubjettiness nSubjettiness(
                        iTauN,
                        fastjet::contrib::OnePass_KT_Axes(),
                        fastjet::contrib::UnnormalizedMeasure(1.0)
                    );
                    
                    tauN = nSubjettiness.result(pseudojet_subStruc);
                    
                    if(tauNm1)
                    {
                        tauNratio = tauN / tauNm1;
                    }
                }
                
                outputInfo->vv_hepTop_tauN_reco.at(iTauN).push_back(tauN);
                outputInfo->vv_hepTop_tauNratio_reco.at(iTauN).push_back(tauNratio);
                
                //printf(
                //    "[%d/%d] "
                //    "Fat jet %d/%d: "
                //    "tau%d (ratio) %0.2f (%0.2f) "
                //    "\n",
                //    
                //    iEvent+1, nEvent,
                //    iFatJet+1, nFatJet,
                //    iTauN, tauN, tauNratio
                //);
                
                tauNm1 = tauN;
            }
            
            
            // Energy correlation
            //double ECFN = 1;
            //double ECFNp1 = 1;
            //double ECFNm1 = 1;
            //
            //for(int iCN = 0; iCN <= _hepTop_CN_max; iCN++)
            //{
            //    double CN = 0;
            //    
            //    if(iCN == 0)
            //    {
            //        fastjet::contrib::EnergyCorrelator energyCorrelatorN(iCN, 1.0);
            //        ECFN = energyCorrelatorN.result(pseudojet_subStruc);
            //    }
            //    
            //    fastjet::contrib::EnergyCorrelator energyCorrelatorNp1(iCN+1, 1.0);
            //    ECFNp1 = energyCorrelatorNp1.result(pseudojet_subStruc);
            //    
            //    if(ECFN)
            //    {
            //        CN = (ECFNp1*ECFNm1) / (ECFN*ECFN);
            //    }
            //    
            //    outputInfo->vv_hepTop_CN_reco.at(iCN).push_back(CN);
            //    
            //    ECFNm1 = ECFN;
            //    ECFN = ECFNp1;
            //}
            //
            //
            //// Shower deconstruction
            //double showerDecon_chi = runShowerDeconstruction(&showerDecon, pseudojet_subStruc);
            //
            //double showerDecon_logChi = -100;
            //
            //if(showerDecon_chi > 0)
            //{
            //    showerDecon_logChi = log(showerDecon_chi);
            //}
            //
            //// Safeguard against occasional NaN values
            //else
            //{
            //    showerDecon_chi = 0;
            //}
            //
            //outputInfo->v_hepTop_showerDecon_chi_reco.push_back(showerDecon_chi);
            //outputInfo->v_hepTop_showerDecon_logChi_reco.push_back(showerDecon_logChi);
            
            
            //// Jet image
            //fastjet::PseudoJet pseudojet_image = fj_fatJet;
            ////fastjet::PseudoJet pseudojet_image_boosted = fj_fatJet;
            //
            //CLHEP::HepLorentzVector hepTop_4mom = PseudoJetToHepLorentzVector(pseudojet_image);
            ////CLHEP::HepLorentzVector hepTop_4mom_boosted = PseudoJetToHepLorentzVector(pseudojet_image);
            //
            ////// Rescale
            ////double rescaleFactor = _jetRescale_m0 / hepTop_4mom_boosted.m();
            ////hepTop_4mom_boosted *= rescaleFactor;
            ////
            ////double boostDir = 1;
            ////
            ////if(hepTop_4mom_boosted.e() < _jetLorentzBoost_E0)
            ////{
            ////    boostDir = -1;
            ////}
            ////
            ////// Boost
            ////CLHEP::Hep3Vector boost_3mom = hepTop_4mom.v().unit();
            ////
            ////double boostGamma = 1.0/(_jetRescale_m0*_jetRescale_m0) * (
            ////    hepTop_4mom_boosted.e() * _jetLorentzBoost_E0 -
            ////    _jetLorentzBoost_P0 * hepTop_4mom_boosted.v().mag()
            ////);
            ////
            ////double boostBeta = std::sqrt(1.0 - 1.0/(boostGamma*boostGamma));
            ////boost_3mom *= boostDir*boostBeta;
            ////
            ////hepTop_4mom.boost(boost_3mom);
            ////
            ////std::vector <fastjet::PseudoJet> v_psJet_consti_boosted;
            ////
            ////for(int iConsti = 0; iConsti < pseudojet_image.constituents().size(); iConsti++)
            ////{
            ////    CLHEP::HepLorentzVector consti_4mom = PseudoJetToHepLorentzVector(pseudojet_image.constituents().at(iConsti));
            ////    
            ////    consti_4mom *= rescaleFactor;
            ////    consti_4mom.boost(boost_3mom);
            ////    
            ////    fastjet::PseudoJet psJet_temp(
            ////        consti_4mom.px(),
            ////        consti_4mom.py(),
            ////        consti_4mom.pz(),
            ////        consti_4mom.e()
            ////    );
            ////    
            ////    v_psJet_consti_boosted.push_back(psJet_temp);
            ////}
            //
            //
            //// Cluster into exactly jets
            //// If there are fewer than 3, returns the constituents
            //fastjet::ClusterSequence fj_fatJetExcSubJet_clustSeq(pseudojet_image.constituents(), *fj_fatJetExcSubJetDef);
            //std::vector <fastjet::PseudoJet> fj_fatJetExcSubJets = fj_fatJetExcSubJet_clustSeq.exclusive_jets_up_to(3);
            //fj_fatJetExcSubJets = sorted_by_E(fj_fatJetExcSubJets);
            
            //printf("Starting image stuff... \n");
            
            TVectorD direc1(2);
            TVectorD direc2(2);
            TVectorD finalTranslation(2);
            
            std::vector <fastjet::PseudoJet> v_GSaxis;
            
            finalTranslation(0) = pseudojet_image.eta() - fj_fatJetExcSubJets.at(0).eta();
            finalTranslation(1) = fj_fatJetExcSubJets.at(0).delta_phi_to(pseudojet_image);
            
            v_GSaxis.push_back(pseudojet_image);
            
            if(nFatJetExcSubJet >= 2)
            {
                direc1(0) = fj_fatJetExcSubJets.at(1).eta() - fj_fatJetExcSubJets.at(0).eta();
                direc1(1) = fj_fatJetExcSubJets.at(0).delta_phi_to(fj_fatJetExcSubJets.at(1));
                
                v_GSaxis.push_back(fj_fatJetExcSubJets.at(0));
            }
            
            else
            {
                v_GSaxis.push_back(fastjet::PseudoJet(0, 0, 0, 0));
            }
            
            
            if(nFatJetExcSubJet >= 3)
            {
                direc2(0) = fj_fatJetExcSubJets.at(2).eta() - fj_fatJetExcSubJets.at(0).eta();
                direc2(1) = fj_fatJetExcSubJets.at(0).delta_phi_to(fj_fatJetExcSubJets.at(2));
                
                v_GSaxis.push_back(fj_fatJetExcSubJets.at(1));
            }
            
            else
            {
                v_GSaxis.push_back(fastjet::PseudoJet(0, 0, 0, 0));
            }
            
            std::vector <std::vector <double> > consti_dEtadPhi_transformed = getTransformedDetaDphi(
                pseudojet_image.constituents(),
                
                fj_fatJetExcSubJets.at(0),
                //pseudojet_image,
                
                direc1,
                direc2,
                finalTranslation
            );
            
            
            //printf(
            //    "[%d/%d] "
            //    "hepTop %d/%d: nConsti %d \n"
            //    "\t E %0.2e, m %0.2e, \n"
            //    "\n",
            //    
            //    iEvent+1, nEvent,
            //    iFatJet+1, nFatJet,
            //    nConsti,
            //    hepTop_4mom.e(), hepTop_4mom.m()
            //);
            
            
            // GS transform
            std::vector <CLHEP::HepLorentzVector> v_consti_boosted = getGStranformed4mom(
                v_GSaxis,
                pseudojet_image.constituents()
            );
            
            CLHEP::HepLorentzVector hepTop_4mom_boosted = getHepLorentzVectorSum(v_consti_boosted);
            
            //printf(
            //    "[%d/%d] "
            //    "hepTop %d/%d: nConsti %d \n"
            //    "\t Original: E %0.2e, m %0.2e, \n"
            //    "\t After GS: E %0.2e, m %0.2e, "
            //    "\n",
            //    
            //    iEvent+1, nEvent,
            //    iFatJet+1, nFatJet,
            //    nConsti,
            //    hepTop_4mom.e(), hepTop_4mom.m(),
            //    hepTop_4mom_boosted.e(), hepTop_4mom_boosted.m()
            //);
            
            // Rescale
            // NOTE: Do not use hepTop_4mom_boosted.m() as it can occasionally be zero (due to precision) if hepTop_4mom.m() is very small
            // Also, very rarely, the mass can be a very small -ve value. Hence use fabs().
            double rescaleFactor = _jetRescale_m0 / fabs(hepTop_4mom.m());
            hepTop_4mom_boosted *= rescaleFactor;
            
            double boostDir = -1;
            
            if(hepTop_4mom_boosted.e() < _jetLorentzBoost_E0)
            {
                boostDir *= -1;
            }
            
            //printf(
            //    "[%d/%d] "
            //    "hepTop %d/%d: nConsti %d \n"
            //    "\t Original      : E %0.2e, m %0.2e, \n"
            //    "\t After  rescale: E %0.2e, m %0.2e, "
            //    "\n",
            //    
            //    iEvent+1, nEvent,
            //    iFatJet+1, nFatJet,
            //    nConsti,
            //    hepTop_4mom.e(), hepTop_4mom.m(),
            //    hepTop_4mom_boosted.e(), hepTop_4mom_boosted.m()
            //);
            
            // Boost
            //CLHEP::Hep3Vector boost_3mom = hepTop_4mom.v().unit();
            //CLHEP::Hep3Vector boost_3mom(1, 0, 0);
            
            double boostGamma = 1.0/(_jetRescale_m0*_jetRescale_m0) * (
                hepTop_4mom_boosted.e() * _jetLorentzBoost_E0 -
                _jetLorentzBoost_P0 * hepTop_4mom_boosted.v().mag()
            );
            
            double boostBeta = boostDir * std::sqrt(1.0 - 1.0/(boostGamma*boostGamma));
            //boost_3mom *= boostBeta;
            
            //hepTop_4mom_boosted.boost(boost_3mom);
            hepTop_4mom_boosted.boostX(boostBeta);
            
            
            // Rescale and boost the constituents
            //#pragma omp parallel for
            for(int iConsti = 0; iConsti < nConsti; iConsti++)
            {
                v_consti_boosted.at(iConsti) *= rescaleFactor;
                v_consti_boosted.at(iConsti).boostX(boostBeta);
            }
            
            CLHEP::HepLorentzVector hepTop_4mom_boosted_sumConsti = getHepLorentzVectorSum(v_consti_boosted);
            
            //printf(
            //    "[%d/%d] "
            //    "hepTop %d/%d: nConsti %d \n"
            //    "\t Original    : E %0.2e, m %0.2e, \n"
            //    "\t After  boost: E %0.2e, m %0.2e, \n"
            //    "\t Sum consti  : E %0.2e, m %0.2e, \n"
            //    "\n",
            //    
            //    iEvent+1, nEvent,
            //    iFatJet+1, nFatJet,
            //    nConsti,
            //    hepTop_4mom.e(), hepTop_4mom.m(),
            //    hepTop_4mom_boosted.e(), hepTop_4mom_boosted.m(),
            //    hepTop_4mom_boosted_sumConsti.e(), hepTop_4mom_boosted_sumConsti.m()
            //);
            
            
            
            
            //fastjet::ClusterSequence fj_fatJetExcSubJet_boosted_clustSeq(v_psJet_consti_boosted, *fj_fatJetExcSubJetDef);
            //std::vector <fastjet::PseudoJet> fj_fatJetExcSubJets_boosted = fj_fatJetExcSubJet_boosted_clustSeq.exclusive_jets_up_to(3);
            //fj_fatJetExcSubJets_boosted = sorted_by_E(fj_fatJetExcSubJets_boosted);
            //
            //int nFatJetExcSubJet_boosted = fj_fatJetExcSubJets_boosted.size();
            //
            //TVectorD direc1_boosted(2);
            //TVectorD direc2_boosted(2);
            //TVectorD finalTranslation_boosted(2);
            //
            ////finalTranslation(0) = pseudojet_image.eta() - fj_fatJetExcSubJets.at(0).eta();
            ////finalTranslation(1) = fj_fatJetExcSubJets.at(0).delta_phi_to(pseudojet_image);
            //
            //if(nFatJetExcSubJet_boosted >= 2)
            //{
            //    direc1_boosted(0) = fj_fatJetExcSubJets_boosted.at(1).eta() - fj_fatJetExcSubJets_boosted.at(0).eta();
            //    direc1_boosted(1) = fj_fatJetExcSubJets_boosted.at(0).delta_phi_to(fj_fatJetExcSubJets_boosted.at(1));
            //    
            //    if(nFatJetExcSubJet_boosted >= 3)
            //    {
            //        direc1_boosted(0) = fj_fatJetExcSubJets_boosted.at(2).eta() - fj_fatJetExcSubJets_boosted.at(0).eta();
            //        direc2_boosted(1) = fj_fatJetExcSubJets_boosted.at(0).delta_phi_to(fj_fatJetExcSubJets_boosted.at(2));
            //    }
            //}
            //
            //std::vector <std::vector <double> > consti_boosted_dEtadPhi_transformed = getTransformedDetaDphi(
            //    v_psJet_consti_boosted,
            //    fj_fatJetExcSubJets_boosted.at(0),
            //    //pseudojet_image,
            //    direc1_boosted,
            //    direc2_boosted,
            //    finalTranslation_boosted
            //);
            
            char name[1000];
            
            sprintf(name, "h2_hepTop%d_E_phiEtaPlane_reco", iFatJet+1);
            TH2F h2_hepTop_fracE_phiEtaPlane_reco(name, name, _image_nBinX, -_fatJetR, _fatJetR, _image_nBinY, -_fatJetR, _fatJetR);
            
            sprintf(name, "h2_hepTop%d_track_E_phiEtaPlane_reco", iFatJet+1);
            TH2F h2_hepTop_track_fracE_phiEtaPlane_reco(name, name, _image_nBinX, -_fatJetR, _fatJetR, _image_nBinY, -_fatJetR, _fatJetR);
            
            sprintf(name, "h2_hepTop%d_photon_E_phiEtaPlane_reco", iFatJet+1);
            TH2F h2_hepTop_photon_fracE_phiEtaPlane_reco(name, name, _image_nBinX, -_fatJetR, _fatJetR, _image_nBinY, -_fatJetR, _fatJetR);
            
            sprintf(name, "h2_hepTop%d_neutralHad_E_phiEtaPlane_reco", iFatJet+1);
            TH2F h2_hepTop_neutralHad_fracE_phiEtaPlane_reco(name, name, _image_nBinX, -_fatJetR, _fatJetR, _image_nBinY, -_fatJetR, _fatJetR);
            
            std::vector <TH2F*> v_h2_hepTop = {
                &h2_hepTop_track_fracE_phiEtaPlane_reco,
                &h2_hepTop_photon_fracE_phiEtaPlane_reco,
                &h2_hepTop_neutralHad_fracE_phiEtaPlane_reco,
            };
            
            
            //
            sprintf(name, "h2_hepTop%d_boosted_E_phiEtaPlane_reco", iFatJet+1);
            TH2F h2_hepTop_boosted_fracE_phiEtaPlane_reco(name, name, _image_nBinX, -1.0, 1.0, _image_nBinY, -1.0, 1.0);
            
            sprintf(name, "h2_hepTop%d_boosted_track_E_phiEtaPlane_reco", iFatJet+1);
            TH2F h2_hepTop_boosted_track_fracE_phiEtaPlane_reco(name, name, _image_nBinX, -1.0, 1.0, _image_nBinY, -1.0, 1.0);
            
            sprintf(name, "h2_hepTop%d_boosted_photon_E_phiEtaPlane_reco", iFatJet+1);
            TH2F h2_hepTop_boosted_photon_fracE_phiEtaPlane_reco(name, name, _image_nBinX, -1.0, 1.0, _image_nBinY, -1.0, 1.0);
            
            sprintf(name, "h2_hepTop%d_boosted_neutralHad_E_phiEtaPlane_reco", iFatJet+1);
            TH2F h2_hepTop_boosted_neutralHad_fracE_phiEtaPlane_reco(name, name, _image_nBinX, -1.0, 1.0, _image_nBinY, -1.0, 1.0);
            
            std::vector <TH2F*> v_h2_hepTop_boosted = {
                &h2_hepTop_boosted_track_fracE_phiEtaPlane_reco,
                &h2_hepTop_boosted_photon_fracE_phiEtaPlane_reco,
                &h2_hepTop_boosted_neutralHad_fracE_phiEtaPlane_reco,
            };
            
            
            //
            sprintf(name, "h2_hepTop%d_boosted_rescaled_E_phiEtaPlane_reco", iFatJet+1);
            TH2F h2_hepTop_boosted_rescaled_fracE_phiEtaPlane_reco(name, name, _image_nBinX, -2.0, 2.0, _image_nBinY, -2.0, 2.0);
            
            sprintf(name, "h2_hepTop%d_boosted_rescaled_track_E_phiEtaPlane_reco", iFatJet+1);
            TH2F h2_hepTop_boosted_rescaled_track_fracE_phiEtaPlane_reco(name, name, 50, -2.0, 2.0, 50, -2.0, 2.0);
            
            sprintf(name, "h2_hepTop%d_boosted_rescaled_photon_E_phiEtaPlane_reco", iFatJet+1);
            TH2F h2_hepTop_boosted_rescaled_photon_fracE_phiEtaPlane_reco(name, name, 50, -2.0, 2.0, 50, -2.0, 2.0);
            
            sprintf(name, "h2_hepTop%d_boosted_rescaled_neutralHad_E_phiEtaPlane_reco", iFatJet+1);
            TH2F h2_hepTop_boosted_rescaled_neutralHad_fracE_phiEtaPlane_reco(name, name, 50, -2.0, 2.0, 50, -2.0, 2.0);
            
            std::vector <TH2F*> v_h2_hepTop_boosted_rescaled = {
                &h2_hepTop_boosted_rescaled_track_fracE_phiEtaPlane_reco,
                &h2_hepTop_boosted_rescaled_photon_fracE_phiEtaPlane_reco,
                &h2_hepTop_boosted_rescaled_neutralHad_fracE_phiEtaPlane_reco,
            };
            
            // ( eta1, ..., etaN )
            // ( phi1, ..., phiN )
            TMatrixD mat_consti_dPhiEta(2, nConsti);
            TMatrixD mat_consti_dPhiEta_pca(2, nConsti);
            
            // ( cov(eta, eta)    cov(eta, phi) )
            // ( cov(eta, phi)    cov(phi, phi) )
            TMatrixD mat_cov(2, 2);
            
            for(int iConsti = 0; iConsti < nConsti; iConsti++)
            {
                fastjet::PseudoJet pseudoJet_consti = pseudojet_image.constituents().at(iConsti);
                
                //fastjet::PseudoJet pseudoJet_consti_boosted = v_psJet_consti_boosted.at(iConsti);
                
                //CLHEP::HepLorentzVector consti_4mom = PseudoJetToHepLorentzVector(pseudoJet_consti);
                
                //double deltaPhi = hepTop_4mom.v().deltaPhi(consti_4mom.v());
                //double deltaEta = hepTop_4mom.eta() - consti_4mom.eta();
                
                //mat_consti_dPhiEta(0, iConsti) = deltaPhi;
                //mat_consti_dPhiEta(1, iConsti) = deltaEta;
                
                h2_hepTop_fracE_phiEtaPlane_reco.Fill(
                    consti_dEtadPhi_transformed.at(iConsti).at(0),
                    consti_dEtadPhi_transformed.at(iConsti).at(1),
                    pseudoJet_consti.e() / hepTop_4mom.e()
                );
                
                v_h2_hepTop.at(pseudoJet_consti.user_index())->Fill(
                    consti_dEtadPhi_transformed.at(iConsti).at(0),
                    consti_dEtadPhi_transformed.at(iConsti).at(1),
                    pseudoJet_consti.e() / hepTop_4mom.e()
                );
                
                //h2_hepTop_fracE_phiEtaPlane_reco.Fill(
                //    consti_dEtadPhi_transformed.at(iConsti).at(0),
                //    consti_dEtadPhi_transformed.at(iConsti).at(1),
                //    pseudoJet_consti.e() / hepTop_4mom.e()
                //);
                
                //v_h2_hepTop.at(pseudoJet_consti.user_index())->Fill(deltaEta, deltaPhi, consti_4mom.e() / hepTop_4mom.e());
                
                
                //h2_hepTop_boosted_fracE_phiEtaPlane_reco.Fill(
                //    consti_boosted_dEtadPhi_transformed.at(iConsti).at(0),
                //    consti_boosted_dEtadPhi_transformed.at(iConsti).at(1),
                //    pseudoJet_consti_boosted.e() / hepTop_4mom_boosted.e()
                //);
                
                
                double X = v_consti_boosted.at(iConsti).py() / v_consti_boosted.at(iConsti).e();
                double Y = v_consti_boosted.at(iConsti).pz() / v_consti_boosted.at(iConsti).e();
                double weight = v_consti_boosted.at(iConsti).e() / _jetLorentzBoost_E0;
                
                double k = 1;
                
                if(v_consti_boosted.at(iConsti).px() < 0)
                {
                    double r = sqrt(X*X + Y*Y);
                    
                    if(r)
                    {
                        k = (2 - r) / r;
                    }
                }
                
                //In the rare cases that a jet as < 3 constituents, the ratio can slightly exceed 1 due to precision, etc.
                weight = min(weight, 1.0);
                
                if(fabs(X) > 1 || fabs(Y) > 1 || fabs(weight) > 1)
                {
                    std::cout << X << ", " << Y << ", " << weight << "\n";
                }
                
                h2_hepTop_boosted_fracE_phiEtaPlane_reco.Fill(X, Y, weight);
                v_h2_hepTop_boosted.at(pseudoJet_consti.user_index())->Fill(X, Y, weight);
                
                
                h2_hepTop_boosted_rescaled_fracE_phiEtaPlane_reco.Fill(k*X, k*Y, weight);
                v_h2_hepTop_boosted_rescaled.at(pseudoJet_consti.user_index())->Fill(k*X, k*Y, weight);
            }
            
            outputInfo->v_h2_hepTop_fracE_phiEtaPlane_reco.push_back(h2_hepTop_fracE_phiEtaPlane_reco);
            outputInfo->v_h2_hepTop_track_fracE_phiEtaPlane_reco.push_back(h2_hepTop_track_fracE_phiEtaPlane_reco);
            outputInfo->v_h2_hepTop_photon_fracE_phiEtaPlane_reco.push_back(h2_hepTop_photon_fracE_phiEtaPlane_reco);
            outputInfo->v_h2_hepTop_neutralHad_fracE_phiEtaPlane_reco.push_back(h2_hepTop_neutralHad_fracE_phiEtaPlane_reco);
            
            outputInfo->v_h2_hepTop_boosted_fracE_phiEtaPlane_reco.push_back(h2_hepTop_boosted_fracE_phiEtaPlane_reco);
            outputInfo->v_h2_hepTop_boosted_track_fracE_phiEtaPlane_reco.push_back(h2_hepTop_boosted_track_fracE_phiEtaPlane_reco);
            outputInfo->v_h2_hepTop_boosted_photon_fracE_phiEtaPlane_reco.push_back(h2_hepTop_boosted_photon_fracE_phiEtaPlane_reco);
            outputInfo->v_h2_hepTop_boosted_neutralHad_fracE_phiEtaPlane_reco.push_back(h2_hepTop_boosted_neutralHad_fracE_phiEtaPlane_reco);
            
            outputInfo->v_h2_hepTop_boosted_rescaled_fracE_phiEtaPlane_reco.push_back(h2_hepTop_boosted_rescaled_fracE_phiEtaPlane_reco);
            outputInfo->v_h2_hepTop_boosted_rescaled_track_fracE_phiEtaPlane_reco.push_back(h2_hepTop_boosted_rescaled_track_fracE_phiEtaPlane_reco);
            outputInfo->v_h2_hepTop_boosted_rescaled_photon_fracE_phiEtaPlane_reco.push_back(h2_hepTop_boosted_rescaled_photon_fracE_phiEtaPlane_reco);
            outputInfo->v_h2_hepTop_boosted_rescaled_neutralHad_fracE_phiEtaPlane_reco.push_back(h2_hepTop_boosted_rescaled_neutralHad_fracE_phiEtaPlane_reco);
            
            
            
            //
            //sprintf(name, "h2_hepTop%d_topRestFrame_fracE_phiEtaPlane_reco", iFatJet+1);
            //TH2F h2_hepTop_topRestFrame_fracE_phiEtaPlane_reco(name, name, _image_nBinX, -1.0, 1.0, _image_nBinY, -1.0, 1.0);
            //
            //sprintf(name, "h2_hepTop%d_topRestFrame_track_E_phiEtaPlane_reco", iFatJet+1);
            //TH2F h2_hepTop_topRestFrame_track_fracE_phiEtaPlane_reco(name, name, 50, -1.0, 1.0, 50, -1.0, 1.0);
            //
            //sprintf(name, "h2_hepTop%d_topRestFrame_photon_E_phiEtaPlane_reco", iFatJet+1);
            //TH2F h2_hepTop_topRestFrame_photon_fracE_phiEtaPlane_reco(name, name, 50, -1.0, 1.0, 50, -1.0, 1.0);
            //
            //sprintf(name, "h2_hepTop%d_topRestFrame_neutralHad_E_phiEtaPlane_reco", iFatJet+1);
            //TH2F h2_hepTop_topRestFrame_neutralHad_fracE_phiEtaPlane_reco(name, name, 50, -1.0, 1.0, 50, -1.0, 1.0);
            //
            //std::vector <TH2F*> v_h2_hepTop_topRestFrame = {
            //    &h2_hepTop_topRestFrame_track_fracE_phiEtaPlane_reco,
            //    &h2_hepTop_topRestFrame_photon_fracE_phiEtaPlane_reco,
            //    &h2_hepTop_topRestFrame_neutralHad_fracE_phiEtaPlane_reco,
            //};
            //
            //
            ////
            //sprintf(name, "h2_hepTop%d_topRestFrame_rescaled_fracE_phiEtaPlane_reco", iFatJet+1);
            //TH2F h2_hepTop_topRestFrame_rescaled_fracE_phiEtaPlane_reco(name, name, _image_nBinX, -2.0, 2.0, _image_nBinY, -2.0, 2.0);
            //
            //sprintf(name, "h2_hepTop%d_topRestFrame_rescaled_track_E_phiEtaPlane_reco", iFatJet+1);
            //TH2F h2_hepTop_topRestFrame_rescaled_track_fracE_phiEtaPlane_reco(name, name, 50, -2.0, 2.0, 50, -2.0, 2.0);
            //
            //sprintf(name, "h2_hepTop%d_topRestFrame_rescaled_photon_E_phiEtaPlane_reco", iFatJet+1);
            //TH2F h2_hepTop_topRestFrame_rescaled_photon_fracE_phiEtaPlane_reco(name, name, 50, -2.0, 2.0, 50, -2.0, 2.0);
            //
            //sprintf(name, "h2_hepTop%d_topRestFrame_rescaled_neutralHad_E_phiEtaPlane_reco", iFatJet+1);
            //TH2F h2_hepTop_topRestFrame_rescaled_neutralHad_fracE_phiEtaPlane_reco(name, name, 50, -2.0, 2.0, 50, -2.0, 2.0);
            //
            //std::vector <TH2F*> v_h2_hepTop_topRestFrame_rescaled = {
            //    &h2_hepTop_topRestFrame_rescaled_track_fracE_phiEtaPlane_reco,
            //    &h2_hepTop_topRestFrame_rescaled_photon_fracE_phiEtaPlane_reco,
            //    &h2_hepTop_topRestFrame_rescaled_neutralHad_fracE_phiEtaPlane_reco,
            //};
            //
            //if(tagger.is_maybe_top() || nFatJetExcSubJet >= 3)
            //{
            //    //printf(
            //    //    "[%d/%d] "
            //    //    "Fatjet %d/%d: "
            //    //    "t size %d, "
            //    //    "t[0] size %d, "
            //    //    "t[1] size %d, "
            //    //    "t[2] size %d, "
            //    //    "\n",
            //    //    
            //    //    iEvent+1, nEvent,
            //    //    iFatJet+1, nFatJet,
            //    //    tagger.t().constituents().size(),
            //    //    tagger.t().pieces().at(0).constituents().size(),
            //    //    tagger.t().pieces().at(1).constituents().size(),
            //    //    tagger.t().pieces().at(2).constituents().size()
            //    //);
            //    
            //    
            //    std::vector <fastjet::PseudoJet> v_GSaxis_topRestFrame;
            //    
            //    v_GSaxis_topRestFrame.push_back(tagger.t());
            //    v_GSaxis_topRestFrame.push_back(tagger.b());
            //    
            //    if((b_4mom_reco+Wj1_4mom_reco).m() < (b_4mom_reco+Wj2_4mom_reco).m())
            //    {
            //        v_GSaxis_topRestFrame.push_back(tagger.W1());
            //    }
            //    
            //    else
            //    {
            //        v_GSaxis_topRestFrame.push_back(tagger.W2());
            //    }
            //    
            //    //v_GSaxis_topRestFrame.push_back(tagger.W1());
            //    //v_GSaxis_topRestFrame.push_back(tagger.W2());
            //    
            //    
            //    std::vector <CLHEP::HepLorentzVector> v_consti_topRestFrame = getGStranformed4mom(
            //        v_GSaxis_topRestFrame,
            //        tagger.t().constituents()
            //    );
            //    
            //    CLHEP::HepLorentzVector t_4mom_topRestFrame_sumConsti = getHepLorentzVectorSum(v_consti_topRestFrame);
            //    
            //    //t_4mom_reco = PseudoJetToHepLorentzVector(tagger.t());
            //    //b_4mom_reco = PseudoJetToHepLorentzVector(tagger.b());
            //    //Wj1_4mom_reco = PseudoJetToHepLorentzVector(tagger.W1());
            //    //Wj2_4mom_reco = PseudoJetToHepLorentzVector(tagger.W2());
            //    
            //    //double boostGamma_topRestFrame = t_4mom_reco.e() / t_4mom_reco.m();
            //    //double boostBeta_topRestFrame = -std::sqrt(1.0 - 1.0/(boostGamma_topRestFrame*boostGamma_topRestFrame));
            //    
            //    double rescaleFactor_topRestFrame = _topRF_jetRescale_m0 / fabs(t_4mom_reco.m());
            //    t_4mom_topRestFrame_sumConsti *= rescaleFactor_topRestFrame;
            //    
            //    double boostDir_topRestFrame = -1;
            //    
            //    if(t_4mom_topRestFrame_sumConsti.e() < _topRF_jetLorentzBoost_E0)
            //    {
            //        boostDir_topRestFrame *= -1;
            //    }
            //    
            //    double boostGamma_topRestFrame = 1.0/(_topRF_jetRescale_m0*_topRF_jetRescale_m0) * (
            //        t_4mom_topRestFrame_sumConsti.e() * _topRF_jetLorentzBoost_E0 -
            //        _topRF_jetLorentzBoost_P0 * t_4mom_topRestFrame_sumConsti.v().mag()
            //    );
            //    
            //    double boostBeta_topRestFrame = boostDir_topRestFrame * std::sqrt(1.0 - 1.0/(boostGamma_topRestFrame*boostGamma_topRestFrame));
            //    t_4mom_topRestFrame_sumConsti.boostX(boostBeta_topRestFrame);
            //    
            //    for(int iConsti = 0; iConsti < v_consti_topRestFrame.size(); iConsti++)
            //    {
            //        v_consti_topRestFrame.at(iConsti) *= rescaleFactor_topRestFrame;
            //        v_consti_topRestFrame.at(iConsti).boostX(boostBeta_topRestFrame);
            //    }
            //    
            //    //t_4mom_topRestFrame_sumConsti = getHepLorentzVectorSum(v_consti_topRestFrame);
            //    
            //    //printf(
            //    //    "[%d/%d] "
            //    //    "Fatjet %d/%d: nConsti %d \n"
            //    //    "\t Original   : E %0.2e, m %0.2e, \n"
            //    //    "\t After boost: E %0.2e, m %0.2e, \n"
            //    //    "\t Sum consti : E %0.2e, m %0.2e, \n"
            //    //    "\n",
            //    //    
            //    //    iEvent+1, nEvent,
            //    //    iFatJet+1, nFatJet,
            //    //    v_consti_topRestFrame.size(),
            //    //    t_4mom_reco.e(), t_4mom_reco.m(),
            //    //    t_4mom_topRestFrame_sumConsti.e(), t_4mom_topRestFrame_sumConsti.m(),
            //    //    getHepLorentzVectorSum(v_consti_topRestFrame).e(), getHepLorentzVectorSum(v_consti_topRestFrame).m()
            //    //);
            //    
            //    for(int iConsti = 0; iConsti < v_consti_topRestFrame.size(); iConsti++)
            //    {
            //        fastjet::PseudoJet pseudoJet_consti = tagger.t().constituents().at(iConsti);
            //        
            //        double X = v_consti_topRestFrame.at(iConsti).py() / v_consti_topRestFrame.at(iConsti).e();
            //        double Y = v_consti_topRestFrame.at(iConsti).pz() / v_consti_topRestFrame.at(iConsti).e();
            //        double weight = v_consti_topRestFrame.at(iConsti).e() / t_4mom_topRestFrame_sumConsti.e();
            //        
            //        if(fabs(X) > 1 || fabs(Y) > 1 || fabs(weight) > 1)
            //        {
            //            std::cout << X << ", " << Y << ", " << weight << "\n";
            //        }
            //        
            //        double k = 1;
            //        
            //        if(v_consti_boosted.at(iConsti).px() < 0)
            //        {
            //            double r = sqrt(X*X + Y*Y);
            //            
            //            if(r)
            //            {
            //                k = (2 - r) / r;
            //            }
            //        }
            //        
            //        h2_hepTop_topRestFrame_fracE_phiEtaPlane_reco.Fill(X, Y, weight);
            //        v_h2_hepTop_topRestFrame.at(pseudoJet_consti.user_index())->Fill(X, Y, weight);
            //        
            //        h2_hepTop_topRestFrame_rescaled_fracE_phiEtaPlane_reco.Fill(k*X, k*Y, weight);
            //        v_h2_hepTop_topRestFrame_rescaled.at(pseudoJet_consti.user_index())->Fill(k*X, k*Y, weight);
            //    }
            //}
            //
            //
            //outputInfo->v_h2_hepTop_topRestFrame_fracE_phiEtaPlane_reco.push_back(h2_hepTop_topRestFrame_fracE_phiEtaPlane_reco);
            //outputInfo->v_h2_hepTop_topRestFrame_track_fracE_phiEtaPlane_reco.push_back(h2_hepTop_topRestFrame_track_fracE_phiEtaPlane_reco);
            //outputInfo->v_h2_hepTop_topRestFrame_photon_fracE_phiEtaPlane_reco.push_back(h2_hepTop_topRestFrame_photon_fracE_phiEtaPlane_reco);
            //outputInfo->v_h2_hepTop_topRestFrame_neutralHad_fracE_phiEtaPlane_reco.push_back(h2_hepTop_topRestFrame_neutralHad_fracE_phiEtaPlane_reco);
            //
            //outputInfo->v_h2_hepTop_topRestFrame_rescaled_fracE_phiEtaPlane_reco.push_back(h2_hepTop_topRestFrame_rescaled_fracE_phiEtaPlane_reco);
            //outputInfo->v_h2_hepTop_topRestFrame_rescaled_track_fracE_phiEtaPlane_reco.push_back(h2_hepTop_topRestFrame_rescaled_track_fracE_phiEtaPlane_reco);
            //outputInfo->v_h2_hepTop_topRestFrame_rescaled_photon_fracE_phiEtaPlane_reco.push_back(h2_hepTop_topRestFrame_rescaled_photon_fracE_phiEtaPlane_reco);
            //outputInfo->v_h2_hepTop_topRestFrame_rescaled_neutralHad_fracE_phiEtaPlane_reco.push_back(h2_hepTop_topRestFrame_rescaled_neutralHad_fracE_phiEtaPlane_reco);
        }
        
        
        // Fill the tree
        outputInfo->fill();
        
        fflush(stdout);
        fflush(stderr);
    }
    
    
    outputFile->cd();
    outputInfo->write();
    
    
    //printf("nWprimePos: %d \n", nWprimePos);
    //printf("nWprimeNeg: %d \n", nWprimeNeg);
    
    
    printf("Number of may-be-top jets: %d \n", jet_nMayBeTop);
    printf("Number of top tagged jets: %d \n", jet_nTopTagged);
    
    outputFile->Close();
    delete outputFile;
    
    //outputInfo->freeMemory();
    
    return 0;
}
