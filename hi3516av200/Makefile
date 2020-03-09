all: hi3516av200_family

hi3519v101:
	cat mux.rdl pad_ctrl.rdl misc_ctrl.rdl peri_crg.rdl peri_pmc.rdl mddrc_ddr_phy.rdl sc_3519v101.rdl hi3519v101.rdl > ../hi3519v101_chip.rdl
hi3516av200:
	cat mux.rdl pad_ctrl.rdl misc_ctrl.rdl peri_crg.rdl peri_pmc.rdl mddrc_ddr_phy.rdl sc_3516av200.rdl hi3516av200.rdl > ../hi3516av200_chip.rdl

hi3516av200_family:
	cat mux.rdl pad_ctrl.rdl misc_ctrl.rdl peri_crg.rdl peri_pmc.rdl mddrc_ddr_phy.rdl sc_3516av200.rdl sc_3519v101.rdl hi3516av200.rdl hi3519v101.rdl > ../hi3516av200.rdl
