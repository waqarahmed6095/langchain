from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

information = """
Asif Ali Zardari[a] (born 26 July 1955) is a Pakistani politician who has been the 14th president of Pakistan since 2024, having held the same office from 2008 to 2013. He is the president of Pakistan People's Party Parliamentarians and was the co-chairperson of Pakistan People's Party from December 2007 until December 2015.[3]

He earlier served as the 11th president of Pakistan from 2008 to 2013, the first president born after Independence. He is the widower of twice-elected Prime Minister of Pakistan Benazir Bhutto. He was a member of the National Assembly of Pakistan from 2018 to 2023, and in 2024.

The son of Hakim Ali Zardari, a landowner from Sindh, Zardari rose to prominence after his marriage to Benazir Bhutto in 1987, who became the Prime Minister of Pakistan after her election in 1988. When Bhutto's government was dismissed by President Ghulam Ishaq Khan in 1990, Zardari was widely criticized for involvement in corruption scandals that led to its collapse.[4][5] When Bhutto was reelected in 1993, Zardari served as Federal Investment Minister and Chairperson of Pakistan Environmental Protection Council. There were increasing tensions between Bhutto's brother Murtaza and Zardari, and Murtaza was killed by police in Karachi on 20 September 1996.[6][7] Bhutto's government was dismissed a month later by President Farooq Leghari, and Zardari was arrested and indicted for Murtaza's murder and for corruption.[8][9]

Although incarcerated, he nominally served in Parliament after being elected to the National Assembly in 1990 and Senate in 1997. He was released from jail in 2004 and went into self-exile to Dubai, but returned when Bhutto was assassinated on 27 December 2007. As the new co-chairman of the PPP, he led his party to victory in the 2008 general elections. He spearheaded a coalition that forced military ruler Pervez Musharraf to resign, and was elected president on 6 September 2008. He was acquitted of various criminal charges the same year.[10][6]

As president, Zardari remained a strong American ally in the war in Afghanistan, despite prevalent public disapproval of the United States following the Raymond Davis incident and the NATO attack in Salala in 2011. Domestically, Zardari achieved the passage of the Eighteenth Amendment to the Constitution in 2010, which constitutionally reduced his presidential powers. His attempt to prevent the reinstatement of Supreme Court judges failed in the face of massive protests led by his political rival Nawaz Sharif. The restored Supreme Court dismissed the PPP's elected Prime Minister Yousaf Raza Gillani for contempt of court in 2012 after Gillani refused to write to the Government of Switzerland to reopen corruption cases against Zardari. Zardari's tenure was also criticised for mishandling nationwide floods in 2010, and growing terrorist violence. Following multiple bombings of Hazaras in Quetta in early 2013, Zardari dismissed his provincial government in Balochistan.

Towards the end of his term, Zardari recorded abysmally low approval ratings, ranging from 11 to 14%.[11][12] After the PPP was heavily defeated in the 2013 general election, Zardari became the country's first elected president to complete his constitutional term on 9 September 2013.[13] His legacy remains divisive, with political observers accusing his administration of corruption and cronyism.[14][15] However, he became president of Pakistan again in March 2024 due to a coalition agreement which was reached following the 2024 Pakistani general election.[16]

Early life and education
Zardari was born on 26 July 1955 in Karachi, Sindh to a prominent Sindhi-Baloch family, and received his upbringing and education in Karachi.[17][18] He belongs to the Zardari family and is the only son of Hakim Ali Zardari, a tribal chief and prominent landowner, and Bilquis Sultana Zardari.[19][20] His paternal grandmother was of Iraqi descent,[21] while his mother was the granddaughter of Hassan Ali Effendi, a Sindhi educationist with Turkish roots who is known as the founder of the Sindh Madressatul Islam.[22][23][24]

In his youth, he led a polo team known as the Zardari Four[25] and pracised boxing.[26] His father owned Bambino[27]—a famous cinema in Karachi—and donated movie equipment to his school.[26] He appeared in a 1969 movie, Salgira, as a child.[28] Zardari's academic background remains a question mark.[26] He received his primary education from Karachi Grammar School. His official biography says he graduated from Cadet College, Petaro in 1972.[29][26] He went to St Patrick's High School, Karachi from 1973 to 1974; a school clerk says he failed his final examination there.[26] In March 2008, he claimed he had graduated from the London School of Business Studies with a bachelor of education degree in the early 1970s.[27] Zardari's official biography states he also attended Pedinton School in Britain.[26][27][30] His British education, however, has not been confirmed, and a search did not turn up any Pedinton School in London.[26][27][30] The issue of his diploma was contentious because a 2002 rule required candidates for Parliament to hold a college degree,[27] but the rule was overturned by Pakistan's Supreme Court in April 2008.[26][30]

Career
Early political career and Benazir Bhutto era
Zardari's initial political career was unsuccessful. In 1983, he lost an election for a district council seat in Nawabshah, a city of Sindh, where his family owned thousands of acres of farmland.[26] He then went into real estate.[26]

He married Benazir Bhutto on 18 December 1987.[31][32] The marriage, which had been arranged, as is customary in Pakistan, was initially described as an unlikely match.[31][32] The lavish sunset ceremony in Karachi was followed by immense night celebrations that included over 100,000 people.[31][32] The marriage enhanced Bhutto's political position in a country where older unmarried women are frowned upon.[31][32] Zardari deferred to his wife's wishes by agreeing to stay out of politics.[32]

In 1988, General Muhammad Zia-ul-Haq died when his plane exploded in midair.[33] A few months later, Bhutto became Pakistan's first female prime minister when her party won 94 of 207 seats contested in the 1988 elections.[34]

Involvement in the first Bhutto Administration and first imprisonment
See also: Corruption charges against Benazir Bhutto and Asif Ali Zardari

Zardari, Benazir Bhutto, and baby Bilawal in a state visit to Andrews Air Force Base in 1989
He generally stayed out of his wife's first administration, but he and his associates became entangled in corruption cases linked to the government.[4] He was largely blamed for the collapse of the Bhutto administration.[5]

After the dismissal of Bhutto's government in August 1990,[35] Benazir Bhutto and Zardari were prohibited from leaving the country by security forces under the direction of the Pakistan Army.[36] During the interim government between August and October, caretaker prime minister Ghulam Mustafa Jatoi, a Bhutto rival, initiated investigations of corruption by the Bhutto administration.[37] Jatoi accused Zardari of using his wife's political position to charge a ten percent commission for obtaining permission to set up any project or to receive loans.[37] He was tagged with the nickname "Mr. Ten Percent".[26]

He was arrested on 10 October 1990 on charges relating to kidnapping and extortion.[35][38] The charges alleged an extortion scheme that involved tying a supposed bomb to a British businessman's leg.[26] The Bhutto family considered the indictment politically motivated and fabricated.[38] In the October 1990 elections, he was elected to the National Assembly while in jail.[39] Bhutto and the PPP staged a walkout from the inaugural session of the National Assembly to protest Zardari's incarceration.[39] He posted $20,000 bail, but his release was blocked by a government ordinance that removed a court's power to release suspects being tried in the terrorist court, which fast-track trials for alleged terrorists.[5] The ordinance was later revoked and a special court acquitted him of bank fraud and conspiracy to murder political opponents.[5] He was freed in February 1993.[5] In March 1994, Zardari was acquitted of bank fraud charges.[40] All other corruption charges relating to Bhutto's first term were dropped or thrown out of the courts.[41]

On 25 March 1991, the hijackers aboard Singapore Airlines Flight 117 demanded Zardari's release among other demands. The hijackers were killed by Singapore Commandos.[42]

Political involvement in the second Bhutto Administration
In April 1993, he became one of the 18 cabinet ministers in the caretaker government that succeeded Nawaz Sharif's first abridged premiership.[43] The caretaker government lasted until the July elections.[43] After Bhutto's election, he served as her Investment Minister,[41][44] chief of the intelligence bureau,[41] and the head of the Federal Investigation Agency.[41] In February 1994, Benazir sent Zardari to meet with Saddam Hussein in Iraq to deliver medicine in exchange for three detained Pakistanis arrested on the ambiguous Kuwait-Iraq border.[45] In April 1994, Zardari denied allegations that he was wielding unregulated influence as a spouse and acting as "de-facto Prime Minister".[46][47] In March 1995, he was appointed chairman of the new Environment Protection Council.[48][49]

During the beginning of the second Bhutto Administration, a Bhutto family feud between Benazir and her mother, Nusrat Bhutto, surfaced over the political future of Murtaza Bhutto, Nusrat's son and Benazir's younger brother.[50] Benazir thanked Zardari for his support.[50] In September 1996, Murtaza and seven others died in a shootout with police in Karachi, while the city was undergoing a three-year civil war.[51][52] At Murtaza's funeral, Nusrat accused Benazir and Zardari of being responsible and vowed to pursue prosecution.[41][51] Ghinwa Bhutto, Murtaza's widow, also accused Zardari of being behind his killing.[41][53] President Farooq Leghari, who would dismiss the Bhutto government seven weeks after Murtaza's death, also suspected Benazir and Zardari's involvement.[41] Several of Pakistan's leading newspapers alleged that Zardari wanted his brother-in-law out of the way because of Murtaza's activities as head of a breakaway faction of the PPP.[41]

In November 1996, Bhutto's government was dismissed by Leghari primarily because of corruption and Murtaza's death.[41] Zardari was arrested in Lahore while attempting to flee the country to Dubai.[41][52]

Jail and exile
The New York Times report
A major report was published in January 1998 by The New York Times detailing Zardari's vast corruption and misuse of public funds.[54] The report discussed $200 million in kickbacks to Zardari and a Pakistani partner for a $4 billion contract with French military contractor Dassault Aviation, in a deal that fell apart only when the Bhutto government was dismissed.[54] It contained details of two payments of $5 million each by a gold bullion dealer in return for a monopoly on gold imports.[54] It had information from Pakistani investigators that the Bhutto family had allegedly accrued more than $1.5 billion in illicit profits through kickbacks in virtually every sphere of government activity.[54] It also reported Zardari's mid-1990s spending spree, which included hundreds of thousands of dollars spent on jewellery.[54] The arrangements made by the Bhutto family for their wealth relied on Western property companies, Western lawyers, and a network of Western friends.[54] The report described how Zardari had arranged secret contracts, painstaking negotiations, and the dismissal of anyone who objected to his dealings.[54]

Citibank, already under fire for its private-banking practices, got into further trouble as a result of the report.[55] Zardari's financial history was one case study in a 1999 U.S. Senate report on vulnerabilities in banking procedures.[56]

Second imprisonment and conviction
In March 1997, Zardari was elected to the Senate while in a Karachi jail.[57][58] In December 1997, he was flown to Islamabad under tight security to take his oath.[57]

In July 1998, he was indicted for corruption in Pakistan after the Swiss government handed over documents to Pakistani authorities relating to money laundering.[59] The Swiss had also indicted him for money laundering.[59] At the same time, in a separate case, he and 18 others were indicted for conspiracy to murder Murtaza Bhutto.[60] After criminal prosecutions began, Citibank closed Zardari's account.[55]

In April 1999, Bhutto and Zardari were convicted for receiving indemnities from a Swiss goods inspection company that was hired to end corruption in the collection of customs duties.[61] The couple received a fine of $8.6 million.[61][62] Both were also sentenced to five years imprisonment, but Bhutto could not be extradited back to Pakistan from her self-imposed exile.[61][62] Zardari was already in jail awaiting trial on separate charges.[61][62] The evidence used against them had been gathered by Swiss investigators and the Pakistani Bureau of Accountability.[61][63]

In May 1999, he was hospitalised after an alleged attempted suicide.[64] He claimed it was a murder attempt by the police.[64]

In August 2003, a Swiss judge convicted Bhutto and Zardari of money laundering and sentenced them to six months imprisonment and a fine of $50,000.[65] In addition, they were required to return $11 million to the Pakistani government.[65] The conviction involved charges relating to kickbacks from two Swiss firms in exchange for customs fraud.[66] In France, Poland, and Switzerland, the couple faced additional allegations.[67]

In November 2004, he was released on bail by court order.[68][69][70] A month later, he was unexpectedly arrested for failing to show up for a hearing on a murder case in Islamabad.[68][69][70] He was placed under house arrest in Karachi.[68][70] A day later, he was released on $5,000 bail.[68][69] His release, rearrest, and then release again was regarded as a sign of growing reconciliation between Musharraf's government and the PPP.[68][69] After his second release in late 2004, he left for exile in Dubai.[26][71]

Exile and legal problems
He returned to Lahore in April 2005.[71][72][73] Police prevented him from holding rallies by escorting him from the airport to his home.[71][72][73] He criticised Pervez Musharraf's government, but rumours of reconciliation between Musharraf and the PPP grew.[72][73] Zardari went back to Dubai in May 2005.[74][75]

In June 2005, he had a heart attack and was treated in the United Arab Emirates.[74][75] A PPP spokesman stated he underwent angioplasty in the United States.[75] In September 2005, he did not show up for a Rawalpindi hearing on corruption charges; the court issued an arrest warrant.[75] His lawyers stated he could not come because he was recovering from his treatment.[75] Following a request by the Rawalpindi court, Interpol issued a red notice in January 2006 against the couple which called on member nations to decide on the couple's extradition.[76][77]

When Bhutto announced in September 2007 her upcoming return to Pakistan, her husband was in New York City undergoing medical treatment.[78] After the October 2007 bombing in Karachi that tainted Bhutto's return, he accused Pakistani intelligence services of being behind the attacks and claimed "it was not done by militants".[79][80] He had not accompanied Bhutto, staying in Dubai with their daughters. Bhutto called for the removal of the chief investigator of the attacks because she claimed he had been involved in Zardari's alleged torture in prison in 1999.[81]

In November 2007, Musharraf instituted emergency rule for six weeks (see Pakistani state of emergency, 2007),[82] under the pretext of rising Islamist militancy, a few days after Bhutto's departure for Dubai to meet with Zardari.[83][84] Immediately after the state of emergency was invoked, Bhutto returned to Pakistan, while Zardari again stayed behind in Dubai.[83][85] Emergency rule was initiated right before the Supreme Court of Pakistan began deliberations on the legality of Musharraf's U.S.-backed proposal—the National Reconciliation Ordinance (NRO)—to drop corruption charges against Bhutto and Zardari in return for a joint Bhutto-Musharraf coalition to govern Pakistan.[83][84] Bhutto and Zardari sympathised with Pervez Musharraf on his feud with the Supreme Court, but simultaneously criticised the imposition of martial law.[83][84][85] Before the Supreme Court could issue a decision, Musharraf replaced its members with his supporters.[83][84]

In the midst of his exile, Zardari had several different legal problems. In Pakistan, Musharraf granted him amnesty for his alleged offences through the National Reconciliation Ordinance, drafted in October 2007.[66] However, the ordinance faced mounting public pressure and an uncompromising judiciary.[66] In addition, it only dealt with charges up to 1999.[66] This left open the possibility of investigations into his alleged involvement in about $2 million in illegal kickbacks to Saddam Hussein, discovered in October 2005, under the oil-for-food program.[66] If the ordinance was rescinded, he would have had to deal with charges relating to evading duties on an armoured BMW, commissions from a Polish tractor manufacturer, and a kickback from a gold bullion dealer.[66] In Switzerland, Bhutto and Zardari appealed the 2003 Swiss conviction, which required the reopening of the case in October 2007.[66] In November 2007, Swiss authorities returned the frozen $60 million to him through offshore companies because of the National Reconciliation Ordinance.[86] In Spain, a criminal investigation was opened over the money laundering for the oil-for-food program because of the illicit profits handled through Spanish firms.[66] In Britain, he was fighting a civil case against the Pakistani government for the proceeds from the liquidation sale of a Surrey mansion.[66] He successfully used his medical diagnosis to postpone a verdict on his British manor trial.[87][88][89]

In exile, he shifted between homes in New York, London, and Dubai, where his three children lived.[26]

On the night of 27 December 2007, he returned to Pakistan following his wife's assassination.[90]

Co-chairperson of the PPP
Bhutto's assassination and succession
Main article: Assassination of Benazir Bhutto
Zardari prevented Bhutto's autopsy in accordance with Islamic principles.[91][92] He and their children attended her funeral, which was held the next day.[93] He denied government allegations that the assassination was sponsored by Al-Qaida.[91][94] He called for an international inquiry into her death and stated that she would still be alive if Musharraf's government had provided adequate protection.[92][95][96] He and his family offered to accept Musharraf's demand to exhume Bhutto's body in exchange for a United Nations inquiry, but Musharraf rejected the proposal.[97]

In Bhutto's political will, she had designated Zardari her successor as party leader.[91][94][98] However, their nineteen-year-old son, Bilawal Bhutto Zardari, became Chairman of the PPP because Zardari favoured Bilawal to represent Bhutto's legacy, in part to avoid division within the party due to his own unpopularity.[91][94][99] He did, however, serve as co-chairman of the PPP for at least three years until Bilawal completed his studies overseas.[91][98][99]

February parliamentary elections and coalition formation
Main article: 2008 Pakistani general election
Zardari called for no delays to the 8 January parliamentary elections and for the participation of all opposition parties.[91] Other major political parties quickly agreed to participate, ending any chance of a boycott.[91][92] Because of the turmoil after the Bhutto assassination, the elections were postponed six weeks to 18 February.[92][100] In January 2008, he suggested that if his party did win a majority, it might form a coalition with Musharraf's Pakistan Muslim League-Q (PML-Q).[100][101] He and Nawaz Sharif, leader of the Pakistan Muslim League (N) party (PML-N), threatened national protests if any vote-rigging was attempted.[101][102] He himself could not run for Parliament because he had not filed election papers in November 2008, back when he had no foreseeable political ambition while Bhutto was alive.[103]

The PPP and the PML-N won the largest and second largest number of seats respectively in the February elections.[103][104] He and Sharif agreed to form a coalition government, ending American hopes of a power-sharing deal between him and Musharraf.[103][104] They agreed to restore the judiciary, but Zardari took a less stringent stance than Sharif.[104][105] He met with U.S. ambassador Anne W. Patterson, who pushed for a pact with Musharraf.[104] To strengthen the new coalition, he reached out to Awami National Party, the Muttahida Qaumi Movement, and Baloch nationalist leaders, who had all boycotted the elections.[106][107]

After weeks of speculation and party infighting, he said he did not want to become prime minister.[107][108][109] In mid-March 2008, he chose Yousaf Raza Gillani for prime minister in a snub to the more politically powerful Makhdoom Amin Fahim.[109]

2008 coalition government
See also: Movement to impeach Pervez Musharraf
He and Sharif agreed in a 9 March 2008 agreement, known as the Murree Declaration, to the reinstatement by 30 April 2008 of 60 judges previously sacked by Musharraf.[110][111] The deadline was later extended to 12 May.[110] He and Sharif held unsuccessful talks at London in May.[110][112] After the coalition failed to restore the judiciary, the PML-N withdrew from the government in mid-May, pulling its ministers out of the cabinet.[110][111][112][113][114] The coalition regrouped, again with the PML-N, and proposed a constitutional amendment that would remove the power of the President to dismiss Parliament.[111][113][114] By late May, the coalition was set in a confrontation with Musharraf.[113][114] At the same time, the government was successful in getting Pakistan readmitted to the Commonwealth.[115]

He and Sharif met in Lahore in June 2008 to discuss Musharraf's removal and the constitutional amendments, which the PML-N viewed as not going far enough to fulfill the Murree declaration.[111][116] He opposed impeachment calls because he claimed the coalition did not have the two-thirds majority in both legislative bodies—National Assembly and Senate.[111][116] He was unwilling to restore the judiciary as divisions in the coalition grew and popular sentiment shifted towards Sharif.[117][118] The coalition criticised the government for barring Sharif from competing in the June by-elections.[117][118][119] Because of the impasses over Musharraf and the judiciary, the coalition could not address rising food shortages and spiraling inflation, which was the highest in 30 years.[111]

In August 2008, Zardari relented, and the coalition agreed to proceed full speed towards Musharraf's impeachment by drafting a charge-sheet against him.[120][121] The coalition charged him with high treason for the 1999 coup and the imposition of martial law.[120] He warned Musharraf against dismissing Parliament, and the coalition selected Gillani instead of Musharraf to represent Pakistan at the 2008 Beijing Olympics.[121][122] On 18 August, Musharraf resigned in order to avoid impeachment.[123][124][125][126] Although Zardari favoured granting Musharraf immunity from prosecution, the coalition could not agree on a decision.[123][124][126] The coalition also could not reach a united stance on the future of the judiciary.[123][124][125][126]

Rise to presidency
Main article: 2008 Pakistani presidential election
Presidential elections were held within three weeks after the departure of Musharraf.[127] Zardari vowed to pursue an unpopular campaign against tribal militancy in Pakistan and had the support of the United States.[127][128][129] He claimed he had a London business school degree to satisfy a prerequisite for the presidency, but his party did not produce a certificate.[130] He was endorsed by the PPP and the Muttahida Qaumi Movement (MQM) for the presidency.[131] The PML-N nominated former justice Saeed-uz-Zaman Siddiqui, while the PML-Q put forth Mushahid Hussain Sayed.[132][133] Zardari won a majority in the Electoral College with 481 of 702 votes.[b][127][133][134][135] He was elected president on 6 September 2008.[c][136][137]

First term as President (2008–2013)
Initial days
At the inauguration on 9 September 2008, Afghan President Hamid Karzai was a guest of honour, which was a signal for much closer cooperation between the two nations in addressing the tribal insurgency along the Afghanistan-Pakistan border.[138][139] After the election, Zardari promised to approve the constitutional provision that removed the President's power to dismiss Parliament, but public scepticism remained on whether he would actually carry out his promise.[127] His economic competence was questioned after allegations that he had raised grain procurement prices through inflationary subsidies and scrapped the capital gains tax.[140] His first parliamentary speech was overshadowed by 20 September Islamabad Marriott Hotel bombing.[141][142][143] A few days later, he went to the United Nations Headquarters in New York City on his first overseas trip as president.[144]


Zardari and Bush meeting in 2008.

Zardari with Emomali Rahmon, Dmitry Medvedev and Hamid Karzai
United Nations visit
See also: Pakistan and the United Nations
From 23 to 26 September 2008, he met with various foreign leaders, including U.S. President George W. Bush and Chinese President Hu Jintao.[145][146][147] He suffered political embarrassment by flirting with U.S. vice presidential candidate Sarah Palin and making tongue-in-cheek comments about her.[148][149][150][151] Although, at the United Nations General Assembly, he publicly condemned U.S drone attacks in Pakistan,[152] The Washington Post reported that he had signed a "secret deal" when he met with senior American officials that arranged for the coordination of Predator strikes and a jointly approved list of prominent targets.[153][154] He and Indian Prime Minister Manmohan Singh agreed to resume peace talks by the end of 2008.[155]

Economic crises
See also: Periods of stagflation in Pakistan
From 14 to 17 October 2008, he was in China[156][157] to negotiate foreign aid, as Pakistan faced the possibility of defaulting on its payments.[158] China refused to offer any aid commitments, but instead promised to provide assistance in the development of two nuclear power plants and more future business investments.[156][158]

After Saudi Arabia, Britain, China, the United States, and the United Arab Emirates refused to provide any bailout,[159] he officially asked the International Monetary Fund (IMF) for assistance in solving Pakistan's balance of payments problem on 22 October.[160]

He went to Saudi Arabia from 4 to 6 November in hopes of obtaining financial aid and securing trade agreements.[161][162] However, leaked cables revealed increasingly strained relations between Zardari and Saudi royalty, primarily because of Saudi distrust of Zardari and preference for Sharif.[163][164][165] Weaker cooperation led to decreased oil subsidies as part of a broader Saudi policy of withholding monetary assistance.[163][165]

In mid-November 2008, Zardari's government officially sent a letter of intent to the IMF regarding a bailout to help increase its foreign exchange reserves.[166] In a $11.3 billion multi-year loan package, Pakistan received a $7.4 billion loan for 2008–10.[167][168] The IMF stipulated stringent reform conditions, which included rebuilding the tax structure and privatising state enterprises.[168] The World Bank and Asian Development Bank withheld a combined $3 billion aid in the 2010–11 fiscal year and the IMF withheld since May 2010 the last segment of its aid package.[168]

In January 2011, the MQM withdrew from the government.[169][170] Zardari's ruling coalition averted a government collapse by accepting the opposition's economic proposals, which restored gas subsidies and abandoned many of the IMF's suggested reforms.[d][169]

In an effort to curb government expenditures, Zardari swore in an "austerity cabinet" in February 2011 which reduced the cabinet from 60 ministers to 22.[171] Asif Zardari is famously known as "Mr. Ten (10) percent" in the Pakistan's political landscape, as he is alleged to demand 10% as kickbacks for the government contracts.[172][173][174]

Foreign policy
Relationship with India
See also: Indo-Pakistani relations
In early October 2008, he received fierce domestic criticism for repeatedly calling Kashmiri nationalists (see Kashmir conflict) in India "terrorists".[175][176] In mid-November 2008, he suggested Pakistan was ready for a no-first-use nuclear policy and called for closer economic ties.[166][177]

The relationship between the two nations was damaged by the November 2008 Mumbai attacks. He initially denied any links between the perpetrators and Pakistan,[178] but the government soon pursued military action against Lashkar-e-Taiba leaders in a 7 December raid.[179][180] India cleared Zardari's government of any direct involvement in the attacks, but simultaneously demanded the extradition of 20 Pakistanis which it alleged had taken part in them.[181] Zardari offered to send Inter-Services Intelligence Director-General Ahmed Shuja Pasha to assist in the investigation.[181]

In June 2009, Zardari met Singh for the first time since the Mumbai attacks at a Shanghai Cooperation Organisation summit in Yekaterinburg, Russia.[182]

On 8 April 2012, President Zardari, along with his son Bilawal Zardari Bhutto, visited Dargah Sharif in Ajmer, India on a private visit. He also met with the Indian prime minister Dr Manmohan Singh.[183][184]


Vice President-Elect Joe Biden meets Zardari in January 2009
War in Afghanistan
See also: Afghanistan–Pakistan relations
The government has had a longstanding conflict in the Federally Administered Tribal Areas (FATA) and Khyber Pakhtunkhwa (KP), Pakistani regions bordering Afghanistan. Diplomatic relations with Afghan President Hamid Karzai improved after Musharraf's departure and Zardari's rise to power.[185] The Obama administration's AfPak policy, through AfPak envoy Richard Holbrooke, reflected the unified approach the United States took in dealing with Afghanistan and Pakistan.[186]

In his first visit to Afghanistan as president in early January 2009, Zardari promised a renewed relationship to improve cooperation.[187][188] In late March, Obama announced a civilian aid package of $7.5 billion over five years in return for cooperation in the AfPak conflict.[189][190][191] In late April, British prime minister Gordon Brown visited Zardari and promised $1 billion over the next four years.[192] In May, Obama held a trilateral summit in Washington D.C., with Karzai and Zardari, where they discussed further cooperation.[193] At Brussels in mid-June, Zardari unsuccessfully sought trade concessions from the European Union; it instead pledged $90 million development aid to curtail tribal influence by insurgents.[194][195][196] After the U.S. Congress passed Obama's civilian aid package in October,[197][198] army generals in the Pakistani military establishment widened the growing rift with Zardari's government and openly criticised U.S. interference.[199][200]


Hamid Karzai, Joe Biden, Barack Obama, and Zardari after the Afghanistan-U.S.-Pakistan trilateral meeting in May 2009
In February 2009, FATA's provincial government officially declared Islamic law in Swat to achieve a ceasefire with the northwestern Pashtun tribes.[201] Because the United States and Britain opposed the measure,[202][203] Zardari did not sign the Swat ceasefire until mid-April, when domestic pressure from Parliament mounted.[201] By the end of April, the agreement collapsed as the Pakistani military pursued an unpopular offensive in the neighbouring Dir district.[204][205]

In September 2010, Zardari and Karzai met in Islamabad and both advocated fighting insurgents rather than trying to end the war with diplomacy.[206] Zardari went to the United States in January 2011 to attend Special Envoy Holbrooke's funeral.[207] Following Osama bin Laden's death in a compound in Abbottabad in May 2011, Obama called Zardari and collaborated on the events.[208]

Reinstatement of the judiciary

Zardari meets Hillary Clinton in May 2009
In February 2009, Zardari and the Musharraf-appointed Supreme Court attempted to disqualify Nawaz Sharif from running in any elections[209] and tried to force his brother Shahbaz Sharif to resign as Chief Minister of Punjab province.[210][211][212] Zardari dismissed the Punjab provincial government[213] and only partially reinstated the judiciary by restoring 56 other judges deposed by Musharraf—but not their former leader, Chief Justice Iftikhar Chaudhry.[214][215] After Nawaz Sharif defied house arrest and rallied with thousands of his supporters,[216] the Sharif brothers vowed to join forces with the Lawyers' Movement in the "Long March".[217][218] Zardari's government gave in to popular pressure[217] and Prime Minister Gilani in an early morning speech on 16 March 2009 promised to reinstate Chaudhry by 21 March.[219][220] Ten judges were reinstated on 16 March, and Chaudry assumed his position on 22 March.[221][222] Zardari's month-long direct control of the Punjab ended on 30 March.[189][222][223]

Nizam-e-Adl Regulation
Further information: Nizam-e-Adl Regulation 2009
In April 2009, President Asif Ali Zardari signed the Nizam-e-Adl Regulation into law. The regulation formally established Sharia law in the Malakand division.[224]

Reduction of presidential powers
See also: Eighteenth Amendment to the Constitution of Pakistan
In late November 2009, Zardari ceded to Prime Minister Gillani the chairmanship of the National Command Authority, Pakistan's nuclear arsenal oversight agency.[225][226]

In December 2009, the Supreme Court ruled that the National Reconciliation Ordinance amnesty was unconstitutional, which cleared the way for the revival of corruption cases against Zardari.[227] Although Zardari had immunity from prosecution because he was president,[86] the end of NRO and his earlier corruption cases challenged the legality of his presidency.[228] Calls for his resignation escalated.[229][230] Zardari, who rarely left the Aiwan-e-Sadr presidential palace,[231] responded with a nationwide spurt of speeches in January 2011.[232] In January 2010, the Supreme Court ordered Pakistan's government to reopen Zardari's corruption charges in Switzerland.[233][234] However, Zardari prevented the MQM-leaning Attorney General, Anwar Mansoor, from filing charges,[235] so Mansoor resigned in protest in early April.[236] That same month, Zardari won a key victory against the judiciary over his corruption trials when Geneva Attorney General Daniel Zappelli stated that Zardari can not be prosecuted under international laws because of his presidential immunity.[237][238] Zardari was supported by Prime Minister Gilani, who defied the Supreme Court order.[239]

In February 2010, Zardari sparked a standoff by attempting to appoint a Supreme Court candidate without the court's approval,[240] but the confrontation ended after he backed down and nominated a candidate acceptable by the court.[241]

In April 2010, after months of political pressure, the government passed the 18th Amendment, which reduced the President to a ceremonial figurehead by stripping the office of the power to dissolve Parliament, to dismiss the Prime Minister, and to appoint military chiefs.[242][243][244] The amendment also lifted the restriction of two terms as prime minister, which enabled Zardari's foremost political rival, Nawaz Sharif, to seek a third term.[242][243][245] The amendment was passed with virtually unanimous support in Parliament[244] and Zardari himself espoused the legislation because of political pressure.[243][245] After the 18th Amendment, Zardari's main power derived from his position as leader of the PPP, which controls the largest bloc in Parliament.[242][243]

In late September 2010, the Supreme Court considered removing presidential immunity.[246] In October, Chief Justice Chaudry met with his colleagues to discuss troubling media rumours that Zardari's government was planning to fire them; Chaudry requested government assurance that the stories were unfounded.[247] In early January 2011, Zardari signed the 19th Amendment, which lessened the likelihood of future clashes between the President and the judiciary by strengthening the power of the Chief Justice in deciding judicial appointments.[248][249]

In March 2011, Zardari delivered his annual parliamentary address to a half-empty chamber because of an opposition walkout.[250]

In November 2012, the Pakistan government in response to the court orders, finally wrote to the Swiss authorities seeking to reopen the corruption cases against Zardari.[251] The Swiss government responded by saying that the corruption cases being time-barred cannot be reopened.[252]

2010 Pakistan floods and Europe tour
The 2010 Pakistan floods began in late July with rain in Khyber Pakhtunkhwa and soon submerged a fifth of Pakistan and affected 20 million people, resulting in one of the nation's largest natural catastrophes. Simultaneously, British prime minister David Cameron sparked a serious diplomatic row with Pakistan during his visit to India[253] by stating that elements within Pakistan were promoting the "export of terror" a week before a planned visit by Zardari to Britain.[254][255][256] Zardari ignored domestic pressure[257][258] and began his European trip in Paris on 1 August, meeting French President Sarkozy.[255][259][260] In France, he drew a rebuke from the U.S. after stating that NATO had "lost the battle for hearts and minds" in the Afghan war.[261][262][263] As the flood's devastation became increasingly evident, he was widely criticised for flying in a helicopter to his Normandy chateau[264][265][266] and dining at Cameron's Chequers countryside home.[267][268][269] Protests within Britain, mainly among the British Pakistani community, grew against his visit.[270][271] The widely expected maiden speech by his son Bilawal was cancelled,[272] as Zardari faced criticism for using the trip to advance Bilawal's political aspirations.[273]

Zardari returned to Pakistan on 10 August.[274] He first visit to an area affected by the flooding was in Sukkur on 12 August.[274] He cancelled the 14 August Independence Day celebrations and instead visited Naushera.[275] He flew over devastated areas with United Nations Secretary-General Ban Ki-moon on 15 August.[276] He left the country on 18 August and attended the four-way Russian summit at Sochi, which included Tajikistan and Afghanistan.[277] On 19 August, he visited Jampur with U.S. Senator John Kerry.[278][279] He ordered local authorities to concentrate efforts to save Shahdadkot from inundation on 24 August.[280]

2011 Dubai hospitalisation
In early December 2011 Zardari flew to Dubai undergoing medical tests and treatment, reportedly for a "small stroke".[281] According to the prime minister, Yousuf Raza Gilani, Zardari sought medical treatment outside of Pakistan because of "threats to his life".[282] He finds himself currently in the midst of the "Memogate" controversy.[282] Zardari left the hospital on 14 December to recuperate at the Persian Gulf, while his son, Bilawal Bhutto Zardari, the chairman of Pakistan Peoples Party, assumed a more prominent role in Pakistan.[283] By 19 December, Zardari had returned to Pakistan.[284]

China–Pakistan Economic Corridor
Pakistan and China on 22 May 2013 signed several agreements and memoranda of understanding (MoUs) that mainly included the long-term China–Pakistan Economic Corridor plan, maritime cooperation and satellite navigation. President Zardari and Chinese Premier Li Keqiang witnessed the signing ceremony as the representatives of the two countries inked the documents at a ceremony held at the Aiwan-e-Sadr. The visit of Premier Keqiang marked the signing of important documents aimed at long-term cooperation between the two countries in multiple areas.[285]

Completion of first presidential tenure
Zardari completed his five-year term on 8 September 2013,[286][287] becoming the first democratically elected president in the 66-year-long history of Pakistan to complete his tenure. He received a guard of honour while leaving the Aiwan-e-Sadr.[288] He was succeeded by Mamnoon Hussain as president.[289]

Between first and second term
He became active in the PPP, which he voted to revamp, after his presidency.[290] He succeeded Ameen Faheem as chairman of PPPP in 2015.[291] In December 2016, he announced that both he and his son Bilawal, would contest the 2018 general election.[292]

In July 2017, during the investigation of the Panama Papers case, Zardari demanded Nawaz Sharif's resignation.[293] In August 2017, Pakistan's anti-corruption court acquitted him from his last pending case in which he was accused along with his late wife, Benazir Bhutto, of laundering illegal kickbacks and maintaining assets beyond known sources of income. The case had dogged him for 19 years.[294][295] His rival Imran Khan believed that Zardari's acquittal was the result of a deal between the PML-N and PPP. However he denied any kind of collaboration.[296] The National Accountability Bureau also challenged the acquittal.[297] On 2 September, after his wife's murder case verdict, which declared Pervez Musharraf a fugitive and convicted two senior police officers, he said that he was not satisfied with the verdict and that he would appeal the judgment as it had acquitted five Pakistani Taliban suspects.[298] In 2019, he was arrested in Islamabad over a money laundering case.[299] An anti-graft court issued an indictment of Zardari on corruption charges on 10 August 2020.[300][301]

Second term as President (since 2024)
On 3 March 2024, the Speaker of the National Assembly of Pakistan confirmed that the Pakistani Parliament would meet on 9 March 2024 to elect a new President of Pakistan,[302] which Zardari won with 411 votes from the national and provincial assemblies against Mahmood Khan Achakzai.[303] He was elected as President on 9 March 2024 by securing 411 electoral votes and his opponent Mahmood Khan Achakzai secured 181 electoral votes.[304] He was sworn in as 14th President on 10 March 2024,[305] the first civilian to be elected as President for a second non-consecutive term.

Opposition reaction
Omar Ayub Khan, the opposition leader in the National Assembly of Pakistan, called Zardari 'illegal'.[306] PTI spokesperson Raoof Hasan described his election "unconstitutional and unacceptable."[307]

Personal life
Family
Zardari and Benazir Bhutto had one son and two daughters. His son, Bilawal Bhutto Zardari, is the current Chairman of the Pakistan Peoples Party. His older daughter, Bakhtawar, was born on 25 January 1990,[308] and his younger daughter, Aseefa, was born on 3 February 1993.[309] After Benazir Bhutto's death, his sister Faryal Talpur became the guardian of his children[18] and he changed Bilawal Zardari's name to Bilawal Bhutto Zardari.[310][311]

His mother died in November 2002, during his detention in jail.[312] His father Hakim Ali Zardari died in May 2011.[313] After that he became the chieftain of the Zardari tribe. However, initially he had decided not to assume leadership and wanted to pass the position to his son Bilawal.[314][313]

Spirituality
Zardari is known to seek the advice of "soothsayers and healers", especially during times of political troubles. He has visited Prof. Ahmad Rafique Akhtar, a well-known Sufi scholar based in Gujar Khan who often counsels government officials and military leaders. During his presidency, he would consult with his then spiritual leader, Pir Mohammad Ejaz, about such matters as travel times and animals were sacrificed during particularly trying periods.[315][316]

Health
His mental health has been a subject of controversy.[87][88] He has repeatedly claimed he was tortured while in prison.[317] He was diagnosed with dementia, major depressive disorder, and post-traumatic stress disorder from 2005 to 2007, which helped influence the verdict of one of his corruption trials.[87][88][89] He now claims he is completely healthy, with only high blood pressure and diabetes.[87][88]

Wealth
In 2005, Daily Pakistan reported he was the second richest man in Pakistan, with an estimated net worth of $1.8 billion.[318] He amassed great wealth while his wife was prime minister.[41] In 2007, he received US$60 million into his Swiss bank account through offshore companies under his name.[86] He was reported to have estates in Surrey, West End of London, Manhattan (a condominium in Belaire Apartments), and Dubai,[25][41] and a 16th-century chateau in Normandy.[265] In Britain, he used a common legal device, the purchase of property through nominees with no family link to the Bhuttos.[41] His homes in Karachi, Lahore, and Islamabad are called Bilawal House I,[319] Bilawal House II,[320] and Zardari House[321] respectively.

Surrey estate
He bought a 365-acre (148-hectare) 20-bedroom luxury estate in Rockwood, Surrey in 1995 through a chain of firms, trusts, and offshore companies in 1994.[18][61][66][322][323] The country home's refurbishment abruptly ended in October 1996, shortly before the end of his wife's second term.[323] He initially denied for eight years that he owned the property, and the bills for the work on the unoccupied mansion were not paid.[66][322] Creditors forced a liquidation sale in 2004, and the Pakistani government claimed the proceeds because the home had been bought with money obtained through corruption.[66] However, he stepped in to claim that he actually was the beneficial owner.[25] As of November 2008, the proceeds were in a liquidator bank account while a civil case continued.[66]

The estate includes two farms, lodgings, staff accommodation, and a basement made into an imitation of a local pub.[18][322] The manor has nine bedrooms and an indoor swimming pool.[323]

He had sent large shipments from Karachi in the 1990s for the refurbishment of Surrey Palace.[66] He has faced allegations from various people, including the daughter of Laila Shahzada,[324] that he acquired stolen art to decorate the palace.[323] He earlier had plans for a helipad, a nine-hole golf course, and a polo pony paddock.[66]

"""
if __name__ == "__main__":
    print("Hello Langchain! \n\n")
    summary_template = """
         Given the information about a person  {information}, who is closest leader to him in America and China.
        Only give name of those leaders and tell reason why they are close to him.
         please apply /no_think mode.
     """
    summary_prompt_template = PromptTemplate(
        input_variables="information", template=summary_template
    )

    llm = ChatOllama(temperature=0, model="qwen3:4b", extract_reasoning=False)

    chain = summary_prompt_template | llm | StrOutputParser()

    res = chain.invoke(input={"information": information})

    print(res)
