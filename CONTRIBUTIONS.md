# CS456 - Mini Group Project 1: Resilient Security Systems

## Redundancy model

### Contributions:

**Victor Troncoso "troncosv"**: 
* checkpoint.py : Implemented functions to save and load the Sentinel's blacklist, preserving its state after a crash.
* backup.py : Implemented a standby Sentinel that restores the saved blacklist and takes over the primary's operations when promoted.
* sentinel.py : Updated the original Sentinel to support checkpoint saving while maintaining its existing firewall, heartbeat functionality, and simulated delay. 
* monitor.py : Updated the code to detect when the sentinel crashes and automatically send a promotion signal to the backup.
  
**Benjamin Mooneyham "Moonshammy"**:

**Matthew Leman "Philojyw"**:
* monitor.py : Improved the monitor's failover reliability by adding crash, failover, and recovery logging, separating the socket polling interval from the failure timeout, and adding repeated promotion attempts while the primary remains unavailable.
* checkpoint.py : Improved checkpoint reliability by adding validation for saved blacklist data, using a consistent checkpoint file path, and making checkpoint writes atomic to reduce the risk of corrupted state.
sentinel.py : Updated checkpoint loading to safely handle missing or invalid checkpoint data.
* backup.py : Updated checkpoint restoration to use the centralized validation logic and safely reject invalid checkpoint data during promotion.
* adversary.py : Updated checkpoint access to use the shared checkpoint path.

**Tyler Short "Tsyber"**: 
* adversary.py : Implemented attacks 1 and 2 to simulate both a heartbeat delay and a corrupted checkpoint

