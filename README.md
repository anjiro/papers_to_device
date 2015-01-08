#README

This project contains a small Python script that copies papers from [Papers 3.0](http://papersapp.com) and up to and from an external drive.

##Why you might need it
Why would you want to do this, when Papers already has Dropbox sync support? I use it with my giant [Sony DPT-S1](https://pro.sony.com/bbsc/ssr/product-DPTS1) PDF reader, which only supports WebDAV-compatible cloud syncing. This way, I have Papers' own Dropbox sync for backups and synchronization to my iPhone, and this script for synchronization to my e-reader.

##How to use it
###From Papers to directory
To copy the currently-selected papers from Papers to another directory:

`papers_to_device -t <target_dir> <target_root>`

The `<target_dir>` argument is where you want the PDF files to end up. The `<target_root>` argument is optional. The script stores a record here of what papers were copied where.

If you leave out `<target_root>`, it will search all of `<target_dir>`'s parent directories for the record.


####Example
First run:

`papers_to_device -t /Volumes/DPT-S1/Papers/Computer_Vision /Volumes/DPT-S1`

subsequent runs:

`papers_to_device -t /Volumes/DPT-S1/Papers/Computer_Vision`

###From directory to Papers
Perhaps you've annotated some PDFs and want to put them back into Papers. This is where the record file comes in—the script remembers where the original Papers file came from and will put your annotated copy back:

`papers_to_device -f <target_root>`

####Example
`papers_to_device -f /Volumes/DPT-S1`