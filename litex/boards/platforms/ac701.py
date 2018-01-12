from litex.build.generic_platform import *
from litex.build.xilinx import XilinxPlatform, XC3SProg, VivadoProgrammer, iMPACT
from litex.build.openocd import OpenOCD

_io = [
    ("ddram", 0,
        Subsignal("a", Pins(
            "M4 J3 J1 L4 K5 M7 K1 M6 H1 K3 N7 L5 L7 N6 L3 K2"),
            IOStandard("SSTL15")),
        Subsignal("ba", Pins("N1 M1 H2"), IOStandard("SSTL15")),
        Subsignal("dq", Pins(
            "AB6 AA8 Y8 AB5 AA5 Y5 Y6 Y7",
            "AF4 AF5 AF3 AE3 AD3 AC3 AB4 AA4",
            "AC2 AB2 AF2 AE2 Y1 Y2 AC1 AB1",
            "Y3 W3 W6 V6 W4 W5 W1 V1",
            "G2 D1 E1 E2 F2 A2 A3 C2",
            "C3 D3 A4 B4 C4 D4 D5 E5",
            "F4 G4 K6 K7 K8 L8 J5 J6",
            "G6 H6 F7 F8 G8 H8 D6 E6"),
            IOStandard("SSTL15"),
            Misc("IN_TERM=UNTUNED_SPLIT_50")),
        Subsignal("dm", Pins("AC6 AC4 AA3 U7 G1 F3 G5 H9"),
            IOStandard("SSTL15")),
        Subsignal("dqs_n", Pins("W8 AE5 AE1 V2 B1 A5 H4 G7"),
            IOStandard("DIFF_SSTL15")),
        Subsignal("dqs_p", Pins("V8 AD5 AD1 V3 C1 B5 J4 H7"),
            IOStandard("DIFF_SSTL15")),
        #Subsignal("odt", Pins("R2 U2"), IOStandard("SSTL15")),
        Subsignal("odt", Pins("R2"), IOStandard("SSTL15")),
        Subsignal("reset_n", Pins("N8"), IOStandard("LVCMOS15")),
        #Subsignal("cs_n", Pins("T3 T2"), IOStandard("SSTL15")),
        Subsignal("cs_n", Pins("T3"), IOStandard("SSTL15")),
        Subsignal("temp_event", Pins("U1"), IOStandard("LVCMOS15")),
        Subsignal("we_n", Pins("R1"), IOStandard("SSTL15")),
        Subsignal("cas_n", Pins("T4"), IOStandard("SSTL15")),
        Subsignal("ras_n", Pins("P1"), IOStandard("SSTL15")),
        #Subsignal("cke", Pins("P4 N4"), IOStandard("SSTL15")),
        Subsignal("cke", Pins("P4"), IOStandard("SSTL15")),
        #Subsignal("clk_n", Pins("L2 N2"), IOStandard("DIFF_SSTL15")),
        #Subsignal("clk_p", Pins("M2 N3"), IOStandard("DIFF_SSTL15")),
        Subsignal("clk_n", Pins("L2"), IOStandard("DIFF_SSTL15")),
        Subsignal("clk_p", Pins("M2"), IOStandard("DIFF_SSTL15")),
        Misc("SLEW=FAST")
    ),

    ("spiflash", 0, # cclk needs to be accessed through STARTUPE2
        Subsignal("dq", Pins("R14 R15 P14 N14")),
        Subsignal("cs_n", Pins("P18")),
        IOStandard("LVCMOS33")
    ),

    ("mmc", 0,
        Subsignal("wp", Pins("R20")),
        Subsignal("det", Pins("P24")),
        Subsignal("cmd", Pins("N23")),
        Subsignal("clk", Pins("N24")),
        Subsignal("dat", Pins("P23 N19 P19 P21")),
        IOStandard("LVCMOS33")
    ),

    ("clk200", 0,   # sysclk
        Subsignal("p", Pins("R3")),
        Subsignal("n", Pins("P3")),
        IOStandard("LVDS_25")
    ),

    ("user_clock", 0,  # configurable clock from Si570
        Subsignal("p"), Pins("M21"),
        Subsignal("n"), Pins("M22"),
        IOStandard("LVDS_25")
    ),

    ("emcclk", 0, Pins("P16"), IOStandard("LVCMOS33")), # not clock-capable

    ("user_sma_clock", 0,
        Subsignal("p"), Pins("J31"),
        Subsignal("n"), Pins("J32"),
        IOStandard("LVDS_25")   # VCCO_VADJ
    ),
    ("user_sma_clock_p", 0, Pins("J31"), IOStandard("LVCMOS25")),   # VCCO_VADJ
    ("user_sma_clock_n", 0, Pins("J32"), IOStandard("LVCMOS25")),   # VCCO_VADJ

    ("mgt_refclk0_mux_sel", 0, Pins("B26 C24"),
        IOStandard("LVCMOS25")  # VCCO_VADJ
    ),

    ("mgt_refclk1_mux_sel", 0, Pins("A24 C26"),
        IOStandard("LVCMOS25")  # VCCO_VADJ
    ),

    ("ephyclk", 0,  # set mgt_refclk0_mux_sel accordingly
        Subsignal("p", Pins("AA13")),
        Subsignal("n", Pins("AB13"))
    ),

    ("si5324_rec_clock", 0,
        Subsignal("p", Pins("D23")),
        Subsignal("n", Pins("D24")),
        IOStandard("LVDS_25")
    ),

    ("si5324_rst_n", 0, Pins("B24"), IOStandard("LVCMOS25")),   # VCCO_VADJ
    ("si5324_int_alm_n", 0, Pins("M19"), IOStandard("LVCMOS33")),

    ("si5324_out0", 0,  # set mgt_refclk0_mux_sel accordingly
        Subsignal("p", Pins("AA13")),
        Subsignal("n", Pins("AB13"))
    ),

    ("si5324_out1", 0,  # set mgt_refclk1_mux_sel accordingly
        Subsignal("p", Pins("AA11")),
        Subsignal("n", Pins("AB11"))
    ),

    ("user_sma_mgt_refclk", 0,  # set mgt_refclk1_mux_sel accordingly
        Subsignal("p", Pins("AA11")),
        Subsignal("n", Pins("AB11"))
    ),

    ("user_sma_mgt_tx", 0,
        Subsignal("p", Pins("AE7")),
        Subsignal("n", Pins("AF7"))
    ),
    ("user_sma_mgt_rx", 0,
        Subsignal("p", Pins("AE11")),
        Subsignal("n", Pins("AF11"))
    ),

    ("pcie_x1", 0,
        Subsignal("rst_n", Pins("M20"), IOStandard("LVCMOS33")),
        Subsignal("wake_n", Pins("K26"), IOStandard("LVCMOS33")),
        Subsignal("clk_p", Pins("F11")),
        Subsignal("clk_n", Pins("E11")),
        Subsignal("tx_p", Pins("D10")),
        Subsignal("tx_n", Pins("C10")),
        Subsignal("rx_p", Pins("D12")),
        Subsignal("rx_n", Pins("C12"))
    ),
    ("pcie_x4", 0,
        Subsignal("rst_n", Pins("M20"), IOStandard("LVCMOS33")),
        Subsignal("wake_n", Pins("K26"), IOStandard("LVCMOS33")),
        Subsignal("clk_p", Pins("F11")),
        Subsignal("clk_n", Pins("E11")),
        Subsignal("tx_p", Pins("D10 B9 D8 B7")),
        Subsignal("tx_n", Pins("C10 A9 C8 A7")),
        Subsignal("rx_p", Pins("D12 B13 D14 B11")),
        Subsignal("rx_n", Pins("C12 A13 C14 A11"))
    ),

    ("sfp_rx", 0,
        Subsignal("n", Pins("AD12")),
        Subsignal("p", Pins("AC12"))
    ),
    ("sfp_tx", 0,
        Subsignal("n", Pins("AD10")),
        Subsignal("p", Pins("AC10"))
    ),
    ("sfp_tx_disable", 0, Pins("R18"), IOStandard("LVCMOS33")),
    ("sfp_los", 0, Pins("R23"), IOStandard("LVCMOS33")),

    ("eth_clocks", 0,
        Subsignal("tx", Pins("U22")),
        Subsignal("rx", Pins("U21")),
        IOStandard("LVCMOS18")
    ),

    ("eth", 0,
        Subsignal("mdio", Pins("T14"), IOStandard("LVCMOS18")),
        Subsignal("mdc", Pins("W18"), IOStandard("LVCMOS18")),
        Subsignal("tx_ctl", Pins("T15"), IOStandard("HSTL")),
        Subsignal("tx_data", Pins("U16 U15 T18 T17"), IOStandard("HSTL")),
        Subsignal("rx_ctl", Pins("U14"), IOStandard("HSTL")),
        Subsignal("rx_data", Pins("U17 V17 V16 V14"), IOStandard("HSTL")),
        Subsignal("rst_n", Pins("V18"), IOStandard("LVCMOS18"))
    ),

    ("serial", 0,
        Subsignal("rts", Pins("W19")),
        Subsignal("cts", Pins("V19")),
        Subsignal("tx", Pins("U19")),
        Subsignal("rx", Pins("T19")),
        IOStandard("LVCMOS18")
    ),

    ("hdmi", 0,
        Subsignal("d", Pins(
            "AA24 Y25 Y26 V26 W26 W25 W24 U26",
            "U25 V24 U20 W23 W20 U24 Y20 V23",
            "AA23 AA25 AB25 AC24 AB24 Y22 Y23 V22")),
        Subsignal("de", Pins("AB26")),
        Subsignal("spdif", Pins("Y21")),
        Subsignal("clk", Pins("V21")),
        Subsignal("vsync", Pins("AC26")),
        Subsignal("hsync", Pins("AA22")),
        Subsignal("int", Pins("W21")),
        Subsignal("spdif_out", Pins("T20")),
        IOStandard("LVCMOS18")
    ),

    ("lcd", 0,
        Subsignal("db", Pins("L25 M24 M25 L22")),
        Subsignal("rw", Pins("L24")),
        Subsignal("rs", Pins("L23")),
        Subsignal("e", Pins("L20")),
        IOStandard("LVCMOS33")
    ),

    ("i2c", 0,
        Subsignal("sda", Pins("K25")),
        Subsignal("scl", Pins("N18")),
        IOStandard("LVCMOS33")
    ),

    ("user_led", 0, Pins("M26"), IOStandard("LVCMOS33")),
    ("user_led", 1, Pins("T24"), IOStandard("LVCMOS33")),
    ("user_led", 2, Pins("T25"), IOStandard("LVCMOS33")),
    ("user_led", 3, Pins("R26"), IOStandard("LVCMOS33")),

    ("user_btn_n", 0, Pins("P6"), IOStandard("SSTL15")),
    ("user_btn_e", 0, Pins("U5"), IOStandard("SSTL15")),
    ("user_btn_s", 0, Pins("T5"), IOStandard("SSTL15")),
    ("user_btn_w", 0, Pins("R5"), IOStandard("SSTL15")),
    ("user_btn_c", 0, Pins("U6"), IOStandard("SSTL15")),

    ("cpu_reset", 0, Pins("U4"), IOStandard("SSTL15")),

    ("user_dip_btn", 0, Pins("R8"), IOStandard("SSTL15")),
    ("user_dip_btn", 1, Pins("P8"), IOStandard("SSTL15")),
    ("user_dip_btn", 2, Pins("R7"), IOStandard("SSTL15")),
    ("user_dip_btn", 3, Pins("R6"), IOStandard("SSTL15")),

    ("rotary", 0,
        Subsignal("b", Pins("P20")),
        Subsignal("push", Pins("N21")),
        Subsignal("a", Pins("N22")),
        IOStandard("LVCMOS33")
    ),

    ("user_sma_gpio_p", 0, Pins("T8"), IOStandard("SSTL15")),
    ("user_sma_gpio_n", 0, Pins("T7"), IOStandard("SSTL15")),

    ("pmod", 0, Pins("P26"), IOStandard("LVCMOS33")),
    ("pmod", 1, Pins("T22"), IOStandard("LVCMOS33")),
    ("pmod", 2, Pins("R22"), IOStandard("LVCMOS33")),
    ("pmod", 3, Pins("T23"), IOStandard("LVCMOS33")),

    ("vadj_on_b", 0, Pins("R16"), IOStandard("LVCMOS33")),

    ("ctrl2_pwrgood", 0, Pins("P15"), IOStandard("LVCMOS33")),

    ("xadc_mux_sel", 0, Pins("B25 A25 A23"),
        IOStandard("LVCMOS25")  # VCCO_VADJ
    ),

    ("fan", 0,
        Subsignal("tach", Pins("J25")),
        Subsignal("pwm", Pins("J26")),
        IOStandard("LVCMOS25")  # VCCO_VADJ
    ),

    ("pmbus", 0,
        Subsignal("clk", Pins("R21")),
        Subsignal("data", Pins("R25")),
        Subsignal("ctrl", Pins("P25")),
        Subsignal("alert", Pins("N26")),
        IOStandard("LVCMOS33")
    ),
]

_connectors = [
    ("HPC", {
        # row A
        "DP1_M2C_P": "AC14",
        "DP1_M2C_N": "AD14",
        "DP1_C2M_P": "AC8",
        "DP1_C2M_N": "AD8",
        # row B
        "GBTCLK1_M2C_P": "AA11",    # set mgt_refclk1_mux_sel accordingly
        "GBTCLK1_M2C_N": "AB11",    # set mgt_refclk1_mux_sel accordingly
        # row C
        "DP0_C2M_P": "AE9",
        "DP0_C2M_N": "AF9",
        "DP0_M2C_P": "AE13",
        "DP0_M2C_N": "AF13",
        "LA06_P": "G19",
        "LA06_N": "F20",
        "LA10_P": "A17",
        "LA10_N": "A18",
        "LA14_P": "C21",
        "LA14_N": "B21",
        "LA18_CC_P": "G20",
        "LA18_CC_N": "G21",
        "LA27_P": "F23",
        "LA27_N": "E23",
        # row D
        "GBTCLK0_M2C_P": "AA13",    # set mgt_refclk0_mux_sel accordingly
        "GBTCLK0_M2C_N": "AB13",    # set mgt_refclk0_mux_sel accordingly
        "LA01_CC_P": "E17",
        "LA01_CC_N": "E18",
        "LA05_P": "G15",
        "LA05_N": "F15",
        "LA09_P": "E16",
        "LA09_N": "D16",
        "LA13_P": "B20",
        "LA13_N": "A20",
        "LA17_CC_P": "K21",
        "LA17_CC_N": "J21",
        "LA23_P": "K20",
        "LA23_N": "J20",
        "LA26_P": "J24",
        "LA26_N": "H24",
        # row E
        "HA01_CC_P": "AB21",
        "HA01_CC_N": "AC21",
        "HA05_P": "AD25",
        "HA05_N": "AD26",
        "HA09_P": "AF19",
        "HA09_N": "AF20",
        "HA13_P": "AC18",
        "HA13_N": "AD18",
        "HA16_P": "AE17",
        "HA16_N": "AF17",
        "HA20_P": "Y16",
        "HA20_N": "Y17",
        # row F
        "PG_M2C": "N17",
        "HA00_CC_P": "AA19",
        "HA00_CC_N": "AB19",
        "HA04_P": "AF24",
        "HA04_N": "AF25",
        "HA08_P": "AD21",
        "HA08_N": "AE21",
        "HA12_P": "AC19",
        "HA12_N": "AD19",
        "HA15_P": "Y18",
        "HA15_N": "AA18",
        "HA19_P": "AC17",
        "HA19_N": "AD17",
        # row G
        "CLK1_M2C_P": "H21",
        "CLK1_M2C_N": "H22",
        "LA00_CC_P": "D18",
        "LA00_CC_N": "C18",
        "LA03_P": "G17",
        "LA03_N": "F17",
        "LA08_P": "C17",
        "LA08_N": "B17",
        "LA12_P": "E20",
        "LA12_N": "D20",
        "LA16_P": "E21",
        "LA16_N": "D21",
        "LA20_P": "M16",
        "LA20_N": "M17",
        "LA22_P": "L17",
        "LA22_N": "L18",
        "LA25_P": "G22",
        "LA25_N": "F22",
        "LA29_P": "G24",
        "LA29_N": "F24",
        "LA31_P": "E26",
        "LA31_N": "D26",
        "LA33_P": "G25",
        "LA33_N": "F25",
        # row H
        "PRSNT_M2C_B": "N16",
        "CLK0_M2C_P": "D19",
        "CLK0_M2C_N": "C19",
        "LA02_P": "H14",
        "LA02_N": "H15",
        "LA04_P": "F18",
        "LA04_N": "F19",
        "LA07_P": "H16",
        "LA07_N": "G16",
        "LA11_P": "B19",
        "LA11_N": "A19",
        "LA15_P": "B22",
        "LA15_N": "A22",
        "LA19_P": "M14",
        "LA19_N": "L14",
        "LA21_P": "J19",
        "LA21_N": "H19",
        "LA24_P": "J18",
        "LA24_N": "H18",
        "LA28_P": "K22",
        "LA28_N": "K23",
        "LA30_P": "E25",
        "LA30_N": "D25",
        "LA32_P": "H26",
        "LA32_N": "G26",
        # row J
        "HA03_P": "AC22",
        "HA03_N": "AC23",
        "HA07_P": "AD23",
        "HA07_N": "AD24",
        "HA11_P": "AD20",
        "HA11_N": "AE20",
        "HA14_P": "AE18",
        "HA14_N": "AF18",
        "HA18_P": "AA17",
        "HA18_N": "AB17",
        "HA22_P": "Y15",
        "HA22_N": "AA15",
        # row K
        "HA02_P": "AE25",
        "HA02_N": "AE26",
        "HA06_P": "AE23",
        "HA06_N": "AF23",
        "HA10_P": "AE22",
        "HA10_N": "AF22",
        "HA17_CC_P": "AA20",
        "HA17_CC_N": "AB20",
        "HA21_P": "AB16",
        "HA21_N": "AC16",
        "HA23_P": "W14",
        "HA23_N": "W15",
        }
    ),
    ("XADC", {
        "VAUX0_P": "K15",
        "VAUX0_N": "J16",
        "VAUX8_P": "J14",
        "VAUX8_N": "J15",
        "GPIO0": "H17",
        "GPIO1": "E22",
        "GPIO2": "K18",
        "GPIO3": "L19",
        }
    ),
]


class Platform(XilinxPlatform):
    default_clk_name = "clk200"
    default_clk_period = 5

    def __init__(self, toolchain="vivado", programmer="vivado"):
        XilinxPlatform.__init__(self, "xc7a200t-fbg676-2", _io, _connectors,
                                toolchain=toolchain)
        self.add_platform_command("""
        set_property CFGBVS VCCO [current_design]
        set_property CONFIG_VOLTAGE 3.3 [current_design]
        """)
        self.toolchain.bitstream_commands = \
            ["set_property BITSTREAM.CONFIG.SPI_BUSWIDTH 4 [current_design]"]
        self.toolchain.additional_commands = \
            ["write_cfgmem -force -format bin -interface spix4 -size 32 "
             "-loadbit \"up 0x0 {build_name}.bit\" -file {build_name}.bin"]
        self.programmer = programmer

    def create_programmer(self):
        if self.programmer == "xc3sprog":
            return XC3SProg("jtaghs1_fast", "bscan_spi_xc7a200t.bit")
        elif self.programmer == "openocd":
            return OpenOCD("kc705.cfg", "bscan_spi_xc7a200t.bit")
        elif self.programmer == "vivado":
            return VivadoProgrammer()
        elif self.programmer == "impact":
            return iMPACT()
        else:
            raise ValueError("{} programmer is not supported".format(
                self.programmer))

    def do_finalize(self, fragment):
        XilinxPlatform.do_finalize(self, fragment)

