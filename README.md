# ENGLISH ASSETS
# GLEXP-Team-RoboTutor-EnglishAssets


### Setup and Configuration

1 Clone this repo to your development computer

```
git clone https://github.com/XPRIZE/GLEXP-Team-RoboTutor-EnglishAssets
```

2 Note that cloning this support repo will require up to a GB of space.

3 Once you have cloned the assets:

  * Attach your target device to the development machine.
  * Ensure the target device is connected by running `adb devices`.
  * Execute:
     * `PUSH_English_StoriesAudio.sh`      (or the respective .bat file if you use Windows)
     * `PUSH_English_TutorAudio.sh` (or .bat)

4 RoboTutor will then have the assets required on the target device (check the _robotutor_assets_ folder).

5 Continue to [build RoboTutor](https://github.com/XPRIZE/GLEXP-Team-RoboTutor-RoboTutor).


#### Zipping Assets

An alternative method to Step 3 above (after cloning) is to zip the assets. This is useful for pushing to remote devices.

  * Execute:
     * `ZIP_English_StoriesAudio.sh`  (or .bat)
     * `ZIP_English_TutorAudio.sh` (or .bat)
  * Zipped folders will be ignored by git (see .gitignore)
  * When placed in the "Download" folder of an Android, RoboTutor will detect these .zip files and install them into the "robotutor_assets" folder.
