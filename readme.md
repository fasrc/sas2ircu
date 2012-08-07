Build rpmbuild/RPMS/x86_64/sas2ircu-5.0-1.el6.x86_64.rpm to monitor this:

    [root@foo ~]# lspci | grep -i lsi
    02:00.0 Serial Attached SCSI controller: LSI Logic / Symbios Logic SAS2008 PCI-Express Fusion-MPT SAS-2 [Falcon] (rev 03)

SAS-2 Integrated RAID Configuration Utility (SAS2IRCU) User Guide Version 1.0 February 2012 DB15-000933-00: http://www.lsi.com/downloads/Public/Host%20Bus%20Adapters/Host%20Bus%20Adapters%20Common%20Files/SAS_SATA_6G_P12/SAS2IRCU_User_Guide.pdf

See also:

- http://hwraid.le-vert.net/wiki/LSIFusionMPTSAS2
- http://exchange.nagios.org/directory/Plugins/Hardware/Storage-Systems/RAID-Controllers/check_sas2ircu/details
- Monitoring hardware RAID: LSI SAS 2008 controller, OMSA - http://lists.us.dell.com/pipermail/linux-poweredge/2012-July/046801.html
