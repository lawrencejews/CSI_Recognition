## CSI-Activity-Recognition
### Using old Tensorflow code to extract data
- NOTE: Run the code from the ROOT not in Models.
- Extract inputfiles and labels -> merge.py
- Run to train CSI extracted data -> current_network.py
### Dataset
We collect dataset using [Linux 802.11n CSI Tool](https://dhalperi.github.io/linux-80211n-csitool/).  

The files with "input_" prefix are WiFi Channel State Information data.  
- 1st column shows timestamp.  
- 2nd - 91st column shows (30 subcarrier * 3 antenna) amplitude.  
- 92nd - 181st column shows (30 subcarrier * 3 antenna) phase.
- Download the public dataset from [click here](https://drive.google.com/file/d/19uH0_z1MBLtmMLh8L4BlNA0w-XAFKipM/view?usp=sharing)
- Inside the dataset, there are 7 different human activities: `bed`, `fall`, `pickup`, `run`, `sitdown`, `standup` and `walk`.
- unzip the Dataset.tar.gz by the following command:
```bash
tar -xzvf Dataset.tar.gz
```
### Requirements
- Numpy
- Tensorflow 2.1+
- sklearn
- pandas
- matplotlib

### Run the Models to Extract & Train 
- Complete extraction and train -> python csi_extractor.py
- Then for Tensorflow 1.0 code -> run merge.py & current_network.py
