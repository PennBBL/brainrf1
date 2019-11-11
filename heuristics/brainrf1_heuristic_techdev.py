#!/usr/bin/env python
"""Heuristic for mapping Brain RF1 scans into BIDS with HiConHiLo stimulation condition visits"""
import os


def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes

    
# **********************************************************************************
# tms session

# condition (run 1)
nback_HiConHiLoWMgated_run1 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_'
    'task-nback_acq-HiConHiLoWMgated1_bold')    
 
# condition (run 2)   
nback_HiConHiLoWMgated_run2 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_'
    'task-nback_acq-HiConHiLoWMgated2_bold')   
    
nback_HiConHiLoWMgated_run3 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_'
    'task-nback_acq-HiConHiLoWMgated3_bold')    
 
# condition (run 2)   
nback_HiConHiLoWMgated_run4 = create_key(
    'sub-{subject}/{session}/func/sub-{subject}_{session}_'
    'task-nback_acq-HiConHiLoWMgated4_bold')   

# **********************************************************************************

def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where

    allowed template fields - follow python string module:

    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """
    last_run = len(seqinfo)

    info = {

        # TMS scans
        nback_HiConHiLoWMgated_run1: [],
        nback_HiConHiLoWMgated_run2: [],
        nback_HiConHiLoWMgated_run3: [],
        nback_HiConHiLoWMgated_run4: [],
        
    }
    
    for s in seqinfo:
        protocol = s.protocol_name.lower()

        # TMS day  
        if "task-nback_acq-HiConHiLoWMgated_run-01" in s.protocol_name:
            info[nback_HiConHiLoWMgated_run1].append(s.series_id)
        elif "task-nback_acq-HiConHiLoWMgated_run-02" in s.protocol_name:
            info[nback_HiConHiLoWMgated_run2].append(s.series_id)
        elif "task-nback_acq-HiConHiLoWMgated_run-03" in s.protocol_name:
            info[nback_HiConHiLoWMgated_run3].append(s.series_id)
        elif "task-nback_acq-HiConHiLoWMgated_run-04" in s.protocol_name:
            info[nback_HiConHiLoWMgated_run4].append(s.series_id)

    return info


# Any extra metadata that might not be automatically added by dcm2niix.

IntendedFor = {
    
    # HiConHiLo    
    }
