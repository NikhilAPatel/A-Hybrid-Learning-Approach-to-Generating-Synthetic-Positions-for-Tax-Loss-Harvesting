import pickle

snp_composition = {'AAPL': 603,'MSFT': 533,'AMZN': 279,'GOOGL': 185,'GOOG': 171,'TSLA': 159,'BRK.B': 149,'UNH': 122,'NVDA': 122,'JNJ': 122,'META': 119,'XOM': 116,'JPM': 100,'V': 94,'PG': 92,'CVX': 91,'MA': 83,'HD': 82,'PFE': 79,'ABBV': 69,'BAC': 67,'LLY': 65,'KO': 64,'AVGO': 62,'PEP': 60,'MRK': 59,'TMO': 57,'VZ': 57,'COST': 55,'ADBE': 53,'ABT': 53,'CMCSA': 51,'DIS': 51,'ACN': 50,'CSCO': 50,'CRM': 49,'MCD': 48,'WMT': 46,'WFC': 46,'DHR': 44,'INTC': 44,'BMY': 44,'LIN': 44,'AMD': 43,'COP': 43,'PM': 42,'QCOM': 41,'NKE': 41,'SSIXX': 40,'TXN': 40,'NEE': 40,'RTX': 39,'T': 39,'AMGN': 37,'UNP': 37,'HON': 35,'LOW': 34,'MDT': 34,'UPS': 34,'IBM': 33,'AMT': 32,'CVS': 32,'CAT': 32,'ANTM': 32,'MS': 31,'ORCL': 31,'INTU': 31,'SPGI': 31,'GS': 28,'LMT': 28,'AMAT': 27,'NOW': 27,'AXP': 27,'PYPL': 27,'DE': 26,'SCHW': 26,'C': 26,'CB': 25,'BKNG': 25,'ADP': 25,'PLD': 24,'CI': 24,'MO': 24,'BLK': 24,'SBUX': 24,'NFLX': 23,'ADI': 23,'MDLZ': 23,'DUK': 22,'GE': 22,'MMM': 22,'EOG': 22,'CCI': 21,'ZTS': 21,'TMUS': 21,'SO': 21,'MMC': 21,'MU': 20,'TGT': 20,'GILD': 20,'ISRG': 20,'BA': 20,'VRTX': 19,'CME': 19,'MPC': 19,'CSX': 19,'PNC': 19,'LRCX': 19,'TJX': 19,'SYK': 19,'BDX': 19,'USB': 19,'SLB': 18,'PGR': 18,'NOC': 18,'PXD': 18,'SHW': 17,'TFC': 17,'CL': 17,'D': 17,'FIS': 17,'REGN': 17,'FCX': 16,'CHTR': 16,'ATVI': 16,'NSC': 16,'EL': 16,'AON': 16,'FISV': 16,'EW': 16,'OXY': 16,'ITW': 16,'WM': 16,'EQIX': 16,'APD': 15,'KLAC': 15,'VLO': 15,'ICE': 15,'HUM': 15,'ETN': 15,'BSX': 15,'DG': 14,'NEM': 14,'EMR': 14,'COF': 14,'GD': 14,'FDX': 14,'GM': 14,'PSX': 14,'MRNA': 14,'F': 14,'PSA': 13,'DOW': 13,'SNPS': 13,'AEP': 13,'NXPI': 13,'LHX': 13,'CNC': 13,'ADM': 13,'HCA': 13,'MET': 13,'MCK': 13,'AIG': 13,'SRE': 13,'KMB': 12,'ROP': 12,'TRV': 12,'DVN': 12,'ADSK': 12,'MAR': 12,'MCO': 12,'HPQ': 12,'CTVA': 12,'EXC': 12,'WMB': 12,'CDNS': 12,'FTNT': 11,'ECL': 11,'AZO': 11,'ORLY': 11,'GIS': 11,'STZ': 11,'PRU': 11,'TEL': 11,'SYY': 11,'EA': 11,'APH': 11,'IQV': 11,'O': 10,'WBD': 10,'ALL': 10,'BK': 10,'PAYX': 10,'A': 10,'HAL': 10,'NUE': 10,'ILMN': 10,'XEL': 10,'CMG': 10,'GPN': 10,'HLT': 10,'MSI': 10,'DLTR': 10,'CTSH': 10,'KR': 10,'DLR': 10,'BAX': 10,'MCHP': 10,'PH': 10,'DD': 10,'JCI': 10,'SBAC': 10,'AFL': 10,'KMI': 10,'WELL': 9,'TT': 9,'CTAS': 9,'PEG': 9,'SPG': 9,'MSCI': 9,'MNST': 9,'IFF': 9,'DFS': 9,'HES': 9,'TDG': 9,'CARR': 9,'YUM': 9,'ED': 9,'DXCM': 8,'CMI': 8,'ALB': 8,'AJG': 8,'ROST': 8,'FAST': 8,'BIIB': 8,'PPG': 8,'RMD': 8,'PCAR': 8,'SIVB': 8,'HSY': 8,'ES': 8,'APTV': 8,'BKR': 8,'IDXX': 8,'OKE': 8,'MTD': 8,'OTIS': 8,'WEC': 8,'TWTR': 8,'WBA': 8,'AMP': 8,'EBAY': 8,'CTRA': 8,'MTB': 8,'LUV': 7,'TSN': 7,'AWK': 7,'WY': 7,'KEYS': 7,'LYB': 7,'FRC': 7,'FANG': 7,'GLW': 7,'AVB': 7,'FITB': 7,'VRSK': 7,'WTW': 7,'RSG': 7,'EIX': 7,'HIG': 7,'EQR': 7,'MRO': 7,'ROK': 7,'CBRE': 7,'AME': 7,'ENPH': 7,'TROW': 7,'DTE': 7,'VICI': 7,'ABC': 6,'TSCO': 6,'FE': 6,'DHI': 6,'LH': 6,'ANSS': 6,'DAL': 6,'CPRT': 6,'GWW': 6,'RF': 6,'LEN': 6,'ULTA': 6,'AEE': 6,'MTCH': 6,'STT': 6,'ZBH': 6,'ARE': 6,'MKC': 6,'FTV': 6,'EFX': 6,'KHC': 6,'ETR': 6,'PPL': 6,'CDW': 6,'WST': 6,'CHD': 6,'STE': 6,'IT': 6,'ODFL': 6,'ANET': 6,'CEG': 6,'MLM': 6,'BALL': 6,'URI': 6,'WAT': 6,'NTRS': 6,'EXR': 6,'HOLX': 5,'IR': 5,'CF': 5,'CMS': 5,'ALGN': 5,'DRE': 5,'TRGP': 5,'APA': 5,'SWKS': 5,'PFG': 5,'RJF': 5,'ZBRA': 5,'HPE': 5,'EXPE': 5,'CNP': 5,'CTLT': 5,'TER': 5,'HBAN': 5,'IP': 5,'AMCR': 5,'J': 5,'K': 5,'MAA': 5,'PARA': 5,'DGX': 5,'SWK': 5,'KEY': 5,'VMC': 5,'TDY': 5,'VRSN': 5,'CINF': 5,'EPAM': 5,'EXPD': 5,'PKI': 5,'CE': 5,'PWR': 5,'GPC': 5,'VTR': 5,'DOV': 5,'SYF': 5,'MOS': 5,'MPWR': 5,'WDC': 5,'CFG': 5,'NDAQ': 5,'FLT': 5,'BBY': 5,'ESS': 5,'GNRC': 5,'POOL': 4,'EVRG': 4,'FMC': 4,'JBHT': 4,'CLX': 4,'SEDG': 4,'NVR': 4,'OMC': 4,'CAG': 4,'DPZ': 4,'CHRW': 4,'GRMN': 4,'SJM': 4,'ATO': 4,'CAH': 4,'PKG': 4,'TXT': 4,'EMN': 4,'DRI': 4,'HST': 4,'MAS': 4,'BRO': 4,'NTAP': 4,'EQT': 4,'LKQ': 4,'NLOK': 4,'AVY': 4,'IEX': 4,'UDR': 4,'LNT': 4,'JKHY': 4,'STX': 4,'HWM': 4,'LDOS': 4,'INCY': 4,'IRM': 4,'AES': 4,'VTRS': 4,'MGM': 4,'LYV': 4,'BXP': 4,'STLD': 4,'BR': 4,'TTWO': 4,'VFC': 4,'CPT': 4,'AKAM': 4,'KMX': 4,'UAL': 4,'WRB': 4,'XYL': 4,'TYL': 4,'DAR': 4,'SBNY': 4,'FDS': 4,'PEAK': 4,'COO': 4,'TRMB': 4,'CSL': 4,'PAYC': 4,'L': 4,'KIM': 4,'TECH': 4,'MOH': 4,'WAB': 4,'BLDR': 4,'OLN': 3,'AA': 3,'FBHS': 3,'PTC': 3,'REG': 3,'WSM': 3,'AAL': 3,'HRL': 3,'RHI': 3,'SCI': 3,'WHR': 3,'SNA': 3,'PHM': 3,'CBOE': 3,'RE': 3,'GGG': 3,'HAS': 3,'BWA': 3,'ABMD': 3,'CCL': 3,'WRK': 3,'AAP': 3,'CZR': 3,'FFIV': 3,'HUBB': 3,'LUMN': 3,'FICO': 3,'CPB': 3,'OC': 3,'LNC': 3,'TPR': 3,'RPM': 3,'FOXA': 3,'BF.B': 3,'TFX': 3,'QRVO': 3,'NDSN': 3,'TAP': 3,'CTXS': 3,'UTHR': 3,'AIZ': 3,'ETSY': 3,'IPG': 3,'AFG': 3,'JLL': 3,'FHN': 3,'CMA': 3,'ALLE': 3,'HSIC': 3,'NRG': 3,'SEE': 3,'NI': 3,'Y': 3,'MKTX': 3,'RRC': 3,'LVS': 3,'RS': 3,'WTRG': 3,'CAR': 3,'CRL': 3,'ACM': 3,'LW': 3,'CLF': 3,'EWBC': 3,'JNPR': 3,'BIO': 3,'RCL': 3,'Other': 2,'AZTA': 2,'ASH': 2,'DXC': 2,'OGN': 2,'LSI': 2,'EEFT': 2,'MPW': 2,'CC': 2,'INGR': 2,'M': 2,'LII': 2,'GTLS': 2,'IIVI': 2,'JAZZ': 2,'KRC': 2,'PNW': 2,'LITE': 2,'STOR': 2,'CIVI': 2,'PNR': 2,'ZION': 2,'OHI': 2,'FSLR': 2,'CNXC': 2,'HP': 2,'BRX': 2,'NFG': 2,'SON': 2,'WWD': 2,'EHC': 2,'TOL': 2,'BBWI': 2,'FRT': 2,'OGE': 2,'DVA': 2,'NLSN': 2,'PCTY': 2,'AYI': 2,'NWL': 2,'KSS': 2,'RNR': 2,'IVZ': 2,'OSK': 2,'ATR': 2,'NVT': 2,'MIDD': 2,'BLD': 2,'HII': 2,'BEN': 2,'NBIX': 2,'RRX': 2,'WBS': 2,'WU': 2,'SYNH': 2,'WYNN': 2,'SNV': 2,'AZPN': 2,'SM': 2,'AMG': 2,'RGEN': 2,'COHR': 2,'FR': 2,'LECO': 2,'LAMR': 2,'ALK': 2,'BRKR': 2,'CGNX': 2,'TREX': 2,'DINO': 2,'CDAY': 2,'NWSA': 2,'GNTX': 2,'RGLD': 2,'WSO': 2,'JBL': 2,'HRB': 2,'WH': 2,'REXR': 2,'MAT': 2,'FAF': 2,'PDCE': 2,'SLAB': 2,'BJ': 2,'ITT': 2,'LSCC': 2,'XRAY': 2,'RGA': 2,'EGP': 2,'SEIC': 2,'MANH': 2,'JEF': 2,'EME': 2,'THC': 2,'AN': 2,'UNM': 2,'PII': 2,'LAD': 2,'DCI': 2,'LEA': 2,'GME': 2,'CDK': 2,'MTDR': 2,'WOLF': 2,'GL': 2,'ORI': 2,'MUSA': 2,'HALO': 2,'MHK': 2,'CABO': 2,'MASI': 2,'ACC': 2,'CASY': 2,'UGI': 2,'MKSI': 2,'AXON': 2,'LFUS': 2,'FIVE': 2,'CW': 2,'VVV': 2,'AGCO': 2,'EXEL': 2,'CHE': 2,'NVST': 2,'CHDN': 2,'NNN': 2,'SLM': 2,'G': 2,'TTC': 2,'KNX': 2,'ARW': 2,'BC': 2,'CIEN': 2,'SAIL': 2,'TTEK': 2,'ACHC': 2,'NOV': 2,'AOS': 2,'PFGC': 2,'DECK': 2,'AIRC': 2,'LPX': 2,'PB': 2,'KBR': 2,'WEX': 2,'SF': 2,'VOYA': 2,'CACI': 2,'CFR': 2,'CBSH': 2,'FFIN': 2,'ROL': 2,'CPRI': 2,'PNFP': 2,'LSTR': 2,'SWN': 2,'UHS': 2,'MUR': 2,'VAC': 1,'SMPL': 1,'RH': 1,'AWR': 1,'KLIC': 1,'STAA': 1,'ACA': 1,'MAN': 1,'SABR': 1,'FORM': 1,'NTCT': 1,'TWNK': 1,'TRUP': 1,'AEIS': 1,'IDA': 1,'NYT': 1,'SAFM': 1,'VC': 1,'ENSG': 1,'MDC': 1,'PEB': 1,'OMI': 1,'HELE': 1,'HI': 1,'MANT': 1,'SFM': 1,'NWE': 1,'HOMB': 1,'AEO': 1,'ONB': 1,'SPSC': 1,'OGS': 1,'KFY': 1,'CR': 1,'GT': 1,'AIT': 1,'MOG.A': 1,'KNSL': 1,'MMS': 1,'LOPE': 1,'IAA': 1,'CNK': 1,'TDC': 1,'UNVR': 1,'SONO': 1,'CVET': 1,'BKH': 1,'TKR': 1,'MXL': 1,'VSCO': 1,'IBP': 1,'CRI': 1,'POST': 1,'AVT': 1,'QLYS': 1,'LXP': 1,'SFBS': 1,'SKX': 1,'ECPG': 1,'CPE': 1,'NSA': 1,'UE': 1,'OFC': 1,'PNM': 1,'NCR': 1,'BOH': 1,'JWN': 1,'ROG': 1,'NWS': 1,'FIX': 1,'HE': 1,'ARCB': 1,'ESNT': 1,'EPR': 1,'MTG': 1,'EXP': 1,'SFNC': 1,'VG': 1,'HR': 1,'PLXS': 1,'SLG': 1,'AM': 1,'IRDM': 1,'TMHC': 1,'HXL': 1,'SHOO': 1,'MTX': 1,'BCC': 1,'HQY': 1,'FHI': 1,'X': 1,'CCOI': 1,'NUS': 1,'CWT': 1,'AAWW': 1,'ITGR': 1,'WLY': 1,'IDCC': 1,'HBI': 1,'JHG': 1,'DRH': 1,'VSH': 1,'PRGO': 1,'EPRT': 1,'XRX': 1,'BRC': 1,'CROX': 1,'WTS': 1,'MSM': 1,'HIW': 1,'RLI': 1,'UBSI': 1,'SRCL': 1,'PCRX': 1,'CBU': 1,'NAVI': 1,'MTZ': 1,'BYD': 1,'KBH': 1,'CVCO': 1,'MTOR': 1,'ENV': 1,'SBRA': 1,'GXO': 1,'IBOC': 1,'SIGI': 1,'SCL': 1,'CNX': 1,'R': 1,'SNX': 1,'KMT': 1,'UMBF': 1,'QDEL': 1,'ASO': 1,'TGNA': 1,'FHB': 1,'FNB': 1,'VSAT': 1,'LTHM': 1,'NSP': 1,'OI': 1,'CSGS': 1,'VIAV': 1,'DKS': 1,'SMG': 1,'SITM': 1,'ADC': 1,'IART': 1,'HAIN': 1,'IBTX': 1,'WSFS': 1,'CADE': 1,'RCM': 1,'FLO': 1,'PRFT': 1,'SPXC': 1,'SEM': 1,'FELE': 1,'BCPC': 1,'NUVA': 1,'AX': 1,'SSD': 1,'FBP': 1,'COOP': 1,'PBF': 1,'UMPQ': 1,'ATI': 1,'KMPR': 1,'NGVT': 1,'EVTC': 1,'TSE': 1,'UNF': 1,'KEX': 1,'REGI': 1,'MLI': 1,'MTH': 1,'FCNCA': 1,'NSIT': 1,'MMSI': 1,'PENN': 1,'SITC': 1,'WAFD': 1,'CYTK': 1,'WIRE': 1,'FCN': 1,'CVBF': 1,'FOX': 1,'LNW': 1,'FSS': 1,'CHH': 1,'BDC': 1,'COKE': 1,'SLGN': 1,'DOC': 1,'SXT': 1,'BCO': 1,'JBT': 1,'UCBI': 1,'PTEN': 1,'FL': 1,'LNTH': 1,'GMED': 1,'NEOG': 1,'ENOV': 1,'THS': 1,'ELY': 1,'UAA': 1,'ALRM': 1,'DAN': 1,'BFH': 1,'SAM': 1,'PDCO': 1,'NATI': 1,'MEDP': 1,'KWR': 1,'PACW': 1,'VSTO': 1,'CBRL': 1,'BHF': 1,'ROIC': 1,'UFPI': 1,'AAON': 1,'CNO': 1,'SRC': 1,'WWE': 1,'TPX': 1,'EXLS': 1,'SANM': 1,'EVR': 1,'HOG': 1,'JBLU': 1,'LHCG': 1,'SIX': 1,'AMN': 1,'CCMP': 1,'AMED': 1,'WTFC': 1,'ONTO': 1,'PCH': 1,'HWC': 1,'NPO': 1,'CRUS': 1,'GATX': 1,'IBKR': 1,'GPI': 1,'PBH': 1,'UNFI': 1,'VNT': 1,'ENS': 1,'UNIT': 1,'WERN': 1,'BRBR': 1,'HUBG': 1,'FULT': 1,'MED': 1,'FLR': 1,'AVA': 1,'INDB': 1,'TPH': 1,'THG': 1,'SIG': 1,'LANC': 1,'ZD': 1,'NARI': 1,'GPRE': 1,'ABM': 1,'SAIA': 1,'ALE': 1,'CHX': 1,'ETRN': 1,'WD': 1,'MLKN': 1,'SBH': 1,'MATX': 1,'TRN': 1,'CELH': 1,'EPC': 1,'LEG': 1,'GPS': 1,'TNL': 1,'VNO': 1,'RL': 1,'FN': 1,'PSB': 1,'NJR': 1,'ITRI': 1,'DTM': 1,'CLH': 1,'LIVN': 1,'LCII': 1,'ABCB': 1,'IOSP': 1,'CPK': 1,'CORT': 1,'DEI': 1,'PK': 1,'MDRX': 1,'POWI': 1,'BKU': 1,'VRTV': 1,'FCPT': 1,'JBGS': 1,'OLED': 1,'AMKR': 1,'RUN': 1,'GO': 1,'KRG': 1,'CATY': 1,'WRE': 1,'BLKB': 1,'GBCI': 1,'VLY': 1,'AVNT': 1,'PRGS': 1,'TRIP': 1,'WING': 1,'TCBI': 1,'DORM': 1,'REZI': 1,'VMI': 1,'COLM': 1,'ABG': 1,'MSA': 1,'DISH': 1,'FWRD': 1,'NYCB': 1,'PZZA': 1,'SR': 1,'CMC': 1,'ICUI': 1,'IIPR': 1,'SWX': 1,'DIOD': 1,'RMBS': 1,'HOPE': 1,'CNMD': 1,'SYNA': 1,'ALGT': 1,'TEX': 1,'UA': 1,'FOXF': 1,'ASGN': 1,'AGO': 1,'SAIC': 1,'THO': 1,'IPGP': 1,'AEL': 1,'OZK': 1,'SJI': 1,'PEN': 1,'WEN': 1,'IRT': 1,'FLS': 1,'EXPO': 1,'NCLH': 1,'FUL': 1,'ARNC': 1,'WDFC': 1,'MRCY': 1,'HPP': 1,'OPCH': 1,'XPO': 1,'BMI': 1,'ARWR': 1,'DY': 1,'XHR': 1,'AJRD': 1,'CBT': 1,'PRI': 1,'ASB': 1,'MDU': 1,'CVLT': 1,'HAE': 1,'THRM': 1,'KAR': 1,'ACIW': 1,'OMCL': 1,'YETI': 1,'JJSF': 1,'ADNT': 1,'SMTC': 1,'CALX': 1,'TXRH': 1,'CUZ': 1,'RYN': 1,'FCFS': 1,'TRMK': 1,'PPBI': 1,'AIN': 1,'PVH': 1,'OLLI': 1,'COTY': 1,'TNDM': 1,'CEIX': 1,'Other': 1,'WCC.PRA': 1,'LBRDP': 1,'ANGO': 1,'BMTX': 1,'RGR': 1,'AMEH': 1,'NEU': 1,'SLVM': 1,'TWO': 1,'CAMP': 1,'XPEL': 1,'CDMO': 1,'ATNI': 1,'ASTE': 1,'DFIN': 1,'CXW': 1,'EMBC': 1,'MYE': 1,'VNDA': 1,'NP': 1,'SLP': 1,'UIS': 1,'MTRN': 1,'HNGR': 1,'TBI': 1,'HFWA': 1,'PMT': 1,'SHEN': 1,'PRDO': 1,'GLT': 1,'AMCX': 1,'LGND': 1,'HTH': 1,'AHH': 1,'NTUS': 1,'QNST': 1,'ABTX': 1,'FLGT': 1,'MYRG': 1,'KAMN': 1,'NXGN': 1,'MODV': 1,'JYNT': 1,'SPNT': 1,'CIR': 1,'PKE': 1,'CASH': 1,'CENT': 1,'PDFS': 1,'SGH': 1,'SWM': 1,'INGN': 1,'HAYN': 1,'DOUG': 1,'PSMT': 1,'ENTA': 1,'CNSL': 1,'WWW': 1,'NYMT': 1,'BBBY': 1,'GEO': 1,'COHU': 1,'MNRO': 1,'WCC': 1,'WGO': 1,'PIPR': 1,'KELYA': 1,'PFBC': 1,'WRLD': 1,'ROCC': 1,'HNI': 1,'HCI': 1,'WSR': 1,'GVA': 1,'PBI': 1,'FARO': 1,'HWKN': 1,'MHO': 1,'YELP': 1,'APOG': 1,'HOUS': 1,'GIII': 1,'BANC': 1,'WNC': 1,'ONL': 1,'GDOT': 1,'RES': 1,'COLL': 1,'SCSC': 1,'KN': 1,'RGP': 1,'JRVR': 1,'SSTK': 1,'MCRI': 1,'DNOW': 1,'LL': 1,'LGIH': 1,'EHTH': 1,'ANIK': 1,'NBR': 1,'SUPN': 1,'COLB': 1,'FBNC': 1,'RWT': 1,'DBI': 1,'AMBC': 1,'LMAT': 1,'UVV': 1,'LQDT': 1,'DBD': 1,'BSIG': 1,'UEIC': 1,'SNEX': 1,'OPI': 1,'KTB': 1,'BKE': 1,'AORT': 1,'HSTM': 1,'ACLS': 1,'GTY': 1,'SBSI': 1,'ENR': 1,'EPAC': 1,'AAT': 1,'STC': 1,'MATW': 1,'STRA': 1,'RYAM': 1,'ARLO': 1,'B': 1,'HMST': 1,'NPK': 1,'ARI': 1,'LYLT': 1,'FF': 1,'RAMP': 1,'MCS': 1,'TVTY': 1,'HZO': 1,'EGRX': 1,'WW': 1,'KD': 1,'TDS': 1,'MCY': 1,'BHE': 1,'HLX': 1,'OIS': 1,'TR': 1,'TBK': 1,'HIBB': 1,'CPS': 1,'STAR': 1,'VBTX': 1,'HRMY': 1,'HSII': 1,'PLCE': 1,'GHL': 1,'OSPN': 1,'AVD': 1,'CMP': 1,'CHEF': 1,'LPI': 1,'AAN': 1,'CALM': 1,'GPMT': 1,'UTL': 1,'IPAR': 1,'GCI': 1,'FOSL': 1,'TG': 1,'GBX': 1,'CHRS': 1,'PGNY': 1,'POWL': 1,'RDNT': 1,'NEO': 1,'CLDT': 1,'QURE': 1,'XNCR': 1,'MGPI': 1,'BLMN': 1,'THRY': 1,'GCP': 1,'WOR': 1,'ICHR': 1,'HCC': 1,'ANIP': 1,'UVE': 1,'TALO': 1,'OXM': 1,'VIR': 1,'IIIN': 1,'GMS': 1,'AMWD': 1,'VRTS': 1,'MTRX': 1,'CPSI': 1,'SHAK': 1,'SAFT': 1,'AOSL': 1,'FCF': 1,'CHUY': 1,'MOV': 1,'TTMI': 1,'CARS': 1,'EIG': 1,'CUBI': 1,'SPWR': 1,'HCSG': 1,'RNST': 1,'VCEL': 1,'VRE': 1,'BCOR': 1,'AVAV': 1,'JBSS': 1,'TMP': 1,'OPRX': 1,'HT': 1,'USPH': 1,'ALG': 1,'MEI': 1,'INT': 1,'NVEE': 1,'RUTH': 1,'EXTN': 1,'BDN': 1,'MAC': 1,'CPF': 1,'BOOM': 1,'PLAY': 1,'CRSR': 1,'ZIMV': 1,'MMI': 1,'NKTR': 1,'FSP': 1,'BHLB': 1,'CNXN': 1,'BOOT': 1,'OFG': 1,'DLX': 1,'UFCS': 1,'UCTT': 1,'ASIX': 1,'KREF': 1,'REX': 1,'DEA': 1,'CMTL': 1,'CATO': 1,'XPER': 1,'NXRT': 1,'VECO': 1,'TGI': 1,'ZUMZ': 1,'VIVO': 1,'LKFN': 1,'PNTG': 1,'HA': 1,'GEF': 1,'MPAA': 1,'VTOL': 1,'HTLD': 1,'DDD': 1,'PPC': 1,'ODP': 1,'TCMD': 1,'TNC': 1,'LTC': 1,'GOGO': 1,'CP': 1,'GES': 1,'FBK': 1,'ESAB': 1,'SCHL': 1,'GNW': 1,'FIZZ': 1,'CCS': 1,'NBHC': 1,'ZYXI': 1,'PATK': 1,'CEVA': 1,'HAFC': 1,'UHT': 1,'CONN': 1,'ATEN': 1,'BANR': 1,'PRAA': 1,'CLB': 1,'ADTN': 1,'AZZ': 1,'RILY': 1,'ILPT': 1,'SVC': 1,'GNL': 1,'CARA': 1,'VVI': 1,'PLAB': 1,'ESE': 1,'EZPW': 1,'EBIX': 1,'FIBK': 1,'LZB': 1,'FBRT': 1,'UFI': 1,'ADUS': 1,'CHS': 1,'SAH': 1,'SSP': 1,'STBA': 1,'TTGT': 1,'CYH': 1,'TWI': 1,'UBA': 1,'ROCK': 1,'WABC': 1,'NFBK': 1,'FDP': 1,'EFC': 1,'AIR': 1,'ANDE': 1,'SKT': 1,'SPPI': 1,'CSII': 1,'EBS': 1,'APEI': 1,'CUTR': 1,'SKYW': 1,'NWBI': 1,'DXPE': 1,'RMAX': 1,'NX': 1,'VGR': 1,'HSKA': 1,'JACK': 1,'GFF': 1,'FBC': 1,'KALU': 1,'GHC': 1,'ANF': 1,'MSEX': 1,'BANF': 1,'MERC': 1,'AMPH': 1,'CVGW': 1,'BGS': 1,'KOP': 1,'FORR': 1,'CCRN': 1,'EGBN': 1,'INVA': 1,'SXC': 1,'CTS': 1,'SPTN': 1,'AGYS': 1,'CHCT': 1,'HMN': 1,'PRA': 1,'HVT': 1,'PUMP': 1,'IVR': 1,'BRKL': 1,'DVAX': 1,'LOCO': 1,'NBTB': 1,'ICLR': 1,'ENVA': 1,'OFIX': 1,'SENEA': 1,'BFS': 1,'SCVL': 1,'DCOM': 1,'PETS': 1,'DGII': 1,'RC': 1,'PRG': 1,'ITOS': 1,'NTGR': 1,'AMSF': 1,'FRGI': 1,'DHC': 1,'EXTR': 1,'DIN': 1,'CRNC': 1,'ORGO': 1,'GKOS': 1,'TBBK': 1,'TRST': 1,'FFBC': 1,'USNA': 1,'OSUR': 1,'WETF': 1,'NWN': 1,'TTEC': 1,'MRTN': 1,'POLY': 1,'INN': 1,'AKR': 1,'PARR': 1,'PFS': 1,'JOE': 1,'MYGN': 1,'APPS': 1,'CRS': 1,'VICR': 1,'ENDP': 1,'CHCO': 1,'BLFS': 1,'PGTI': 1,'CAKE': 1,'HSC': 1,'SLQT': 1,'BIG': 1,'NR': 1,'ELF': 1,'HLIT': 1,'ETD': 1,'SNBR': 1,'BATL': 1,'ZEUS': 1,'GCO': 1,'CSR': 1,'EGHT': 1,'EAT': 1,'PAHC': 1,'LPSN': 1,'VREX': 1,'CTRE': 1,'SRDX': 1,'MD': 1,'TREE': 1,'ATGE': 1,'AXL': 1,'CCSI': 1,'LNN': 1,'NMIH': 1,'TMST': 1,'MLAB': 1,'DRQ': 1,'RCUS': 1,'RCII': 1,'RGNX': 1,'OSIS': 1,'SXI': 1,'PLUS': 1,'PLMR': 1,'BJRI': 1,'AVNS': 1,'SAFE': 1,'SMP': 1,'TILE': 1,'GDEN': 1,'TRMR': 1,'SLCA': 1,'CENX': 1,'VRA': 1,'CAL': 1,'CENTA': 1,'RPT': 1,'CRVL': 1,'CFFN': 1,'SBCF': 1,'AROC': 1,'IRBT': 1,'PRK': 1,'ARR': 1,'CRMT': 1,'RRGB': 1,'OII': 1,'CLW': 1,'ALEX': 1,'NIHD': 1,'PRLB': 1,'URBN': 1,'LPG': 1,'TUP': 1,'NBRWF': 1,'Other': 1}

snp_comp_file_path = "pickles/snp_composition.obj"


file_snp_comp = open(snp_comp_file_path, 'wb')
pickle.dump(snp_composition, file_snp_comp)
file_snp_comp.close()
