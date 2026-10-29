# CS456 - Mini Group Project 1: Resilient Security Systems

## Redundancy model

### Contributions:

**Victor Troncoso "troncosv"**: 
* checkpoint.py : Implemented functions to save and load the Sentinel's blacklist, preserving its state after a crash.
* backup.py : Implemented a standby Sentinel that restores the saved blacklist and takes over the primary's operations when promoted.
* sentinel.py : Updated the original Sentinel to support checkpoint saving while maintaining its existing firewall and heartbeat functionality.
  
**Benjamin Mooneyham "Moonshammy"**:

**Matthew Leman "Philojyw"**:

**Tyler Short "Tsyber"**: Implementation of adversary, attack 1.

