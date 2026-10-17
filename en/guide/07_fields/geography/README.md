# Social and economic geography: field overview

This page explains how research actually works in human geography (social, economic, urban, cultural, political, and development geography, among others) and in spatial analysis and geographic information systems (GIS) research in the social sciences. That means fieldwork in "places," analysis of data that carry coordinates, and the problems these two bring with them: researcher positionality, field ethics and safety, conclusions that change with how spatial units are drawn, participants' location privacy, and the reproducibility of geographic research. Physical geography (geomorphology, climate, hydrology, and so on) is covered on the [Earth and environmental sciences page](../earth-environmental-sciences/README.md). Where geography overlaps with sociology (interviews, ethnographic ethics, data archiving), see the [Sociology page](../sociology/README.md); this page covers only what geography adds. For what applies in every field, see the chapters listed in [The research journey at a glance](../../00_start-here/research-journey.md) and [Throughout the project](../../08_throughout/README.md). For the research strategies the field commonly uses and the evidence each one relies on, see [Common strategies and standards of evidence](#common-strategies-and-standards-of-evidence).

**After reading this page, you should be able to:**

- explain what each of the main approaches in human geography is good at, and how they are combined;
- know what two representative sets of geography ethics rules say: the American Association of Geographers' (AAG) statement of professional ethics for its members, and the code that the Royal Geographical Society (with the Institute of British Geographers) (RGS-IBG) sets for the projects it funds;
- explain in plain words the modifiable areal unit problem, the ecological fallacy, and the uncertain geographic context problem, and know how to address them in a paper;
- protect participants' privacy when you collect, analyze, and publish location data;
- make your spatial analysis reproducible by others.

---

## How research works in this field

### One field, several approaches

The ethics statement of the American Association of Geographers (AAG) opens by saying that geography spans the natural sciences, the social sciences, and the humanities and arts[^aag2024ethics-e1]. Within human geography, research roughly follows three approaches (this grouping is our own `[Our analysis]`):

- **Qualitative fieldwork**: you go to a place and use interviews, participant observation, ethnography, and participatory mapping (drawing maps together with local people) to understand the relationship between people and place `[Our analysis]`. The AAG sees doing research "with, rather than on" participants, and avoiding extractive research, as an important sign of respect[^aag2024ethics-e4].
- **Quantitative spatial analysis and GIS**: you use data with locations (censuses, surveys, GPS tracks, remote sensing imagery, social media check-ins, and so on) for spatial statistics, spatial regression, and mapping `[Our analysis]`. This kind of analysis requires you to fix many parameters in advance, such as the scale of analysis and how "neighboring" is represented[^kedron2021reproducibility-e2]; later sections explain why this matters so much.
- **Mixed methods**: combining the two. For example, the geographer Mei-Po Kwan argued in a 2018 paper that when you measure what environment a person is exposed to, adding qualitative information on how that person perceives and understands their environment seems to help mitigate the "uncertain geographic context problem" described below[^kwan2018limits-e4].

Within one department, researchers following these approaches may have very different ideas of what good research is `[Our analysis]`. As a newcomer, first find out which tradition your advisor and your target journals belong to, and then decide how to write your methods section `[Our analysis]`.

### Publishing and authorship

- **Conference papers (GIScience).** Geographic information science (GIScience, the study of how geographic information is acquired, represented, and analyzed) has its own academic conferences. For example, the Association of Geographic Information Laboratories in Europe (AGILE) has held a conference every year since 1998[^nust2018reproducible-e1]; since 2007 it has had a full paper track and a short paper track, and the short papers are published free on the AGILE website[^nust2018reproducible-e2]. Our sources do not cover the standing of journals and monographs, review times, or authorship-order conventions in the various branches of human geography; follow your advisor or your target journal.
- **Some journals require open data.** According to Kedron and colleagues, writing in 2020, the *International Journal of Geographical Information Science* (IJGIS) requires authors to make data and research materials freely available and aligned with the FAIR principles (findable, accessible, interoperable, reusable)[^kedron2021reproducibility-e10].
- **The AAG rule in the US: disclose your funding.** Publishing in an AAG journal, or presenting at the AAG Annual Meeting or a regional division meeting, requires you to disclose your funding sources[^aag2024ethics-e16].
- **Settle authorship at the start.** The AAG ethics statement requires that the scope of collaboration, each party's rights and responsibilities, co-authorship, and acknowledgment be established openly and fairly at the outset[^aag2024ethics-e8]. The UK RGS-IBG's code for its grants program requires that local collaborators be credited in data ownership and in authorship of papers[^rgsgrantscode-e5]. For general principles of authorship, see [Authorship and citation](../../08_throughout/integrity_and_ethics.md#5-authorship-citation-and-conflicts-of-interest-give-every-contributor-due-credit) in Throughout the project.

---

## How this field differs from others

| | Social and economic geography | Comparison |
|---|---|---|
| What is studied | People and places `[Our analysis]`; the AAG holds that all geographical knowledge is "situated," tied to the people and settings that produce it[^aag2024ethics-e3] | Sociology focuses on social relationships and social structure; see the [Sociology page](../sociology/README.md) `[Our analysis]` |
| Special risks of the data | Coordinates themselves can identify people: even anonymized trajectory data can often be re-identified[^malekzadeh2026ethical-e1] | For handling data in general, see [Data science](../../06_methods/data_science.md); location data need an extra layer of protection `[Our analysis]` |
| Whether results hold elsewhere | Whether you should expect a result to hold in another place is itself contested[^kedron2021reproducibility-e6] | Many experimental fields treat "another lab can repeat it" as the test of a result `[Our analysis]` |
| Fieldwork | Fieldwork is part of geographical research and often involves travel[^rgsgrantscode-e6]; the UK RGS-IBG requires the projects it funds to also pass ethics review in the host country[^rgsgrantscode-e3] | For field safety and permits in physical geography, see the [Earth and environmental sciences page](../earth-environmental-sciences/README.md#fieldwork-sort-out-safety-and-permits-first) |

---

## Norms and reporting standards in this field

Below, two sets of rules serve as examples. Each binds particular people; neither is a worldwide rule for geography:

- **The AAG Statement of Professional Ethics** (revised in 2024[^aag2024ethics-e18]). AAG members must follow the association's professional conduct policy; many geographers must also meet the human subjects ethics requirements of their institutions and funders[^aag2024ethics-e2].
- **The RGS-IBG Code of Practice for its grants program**, plus its safety and ethics guidance for grant applicants. The code's ethics provisions apply to research the society supports: research it funds, research presented at its conferences, and research published in its journals[^rgsgrantscode-e1].

For research outside the reach of these two bodies, follow the rules of your country, your institution, and your funder `[Our analysis]`.

### Field ethics: protect people and places first

- **Doing no harm comes before gaining knowledge.** The AAG statement says that the obligation to do no harm supersedes the goals of seeking or communicating new knowledge[^aag2024ethics-e6].
- **Be aware of your own power.** The AAG warns that researchers often occupy powerful positions relative to participants, and it is all too easy to be unaware of the impact of these power imbalances[^aag2024ethics-e7].
- **Consent is an ongoing dialogue.** The AAG requires informed consent to be built into project design and negotiated continuously during implementation[^aag2024ethics-e9]. What matters is the quality of consent, not its format, and the right to refuse belongs to whole communities, not only to individuals[^aag2024ethics-e11].
- **Get ethics approval where it exists; otherwise ask the community.** The AAG requires that where a country has an institutional review board (IRB, an ethics review committee) or a similar process, you must obtain approval; where it does not, you should obtain permission from the relevant communities[^aag2024ethics-e10]. The UK RGS-IBG also requires the projects it funds to get approval from the host country's ethics committee where one exists, even if your own institution has already approved the project[^rgsgrantscode-e3].
- **Say where the money comes from when you ask for consent.** The AAG requires you to disclose all funding sources and partners, in an understandable way, at the time you request consent[^aag2024ethics-e15].
- **Involve local people, and bring the results back.** The RGS-IBG code requires local collaborators, communities, and participants to be involved throughout, from planning to feedback after the research[^rgsgrantscode-e4]; the AAG requires that, where appropriate, results be shared with participants and affected communities in a form they can understand[^aag2024ethics-e12].
- **Have a reason to travel.** In its "sustainable research" section, the RGS-IBG code requires a clear rationale for travel and for the choice of destination[^rgsgrantscode-e6].

For general practice in human subjects ethics, see [When research involves people, protect them first](../../08_throughout/integrity_and_ethics.md#4-when-research-involves-people-or-could-harm-others-protect-people-first) in Throughout the project; for pseudonyms, gatekeepers, the limits of confidentiality, and other issues in long-term fieldwork, see the [Sociology page](../sociology/README.md#problems-specific-to-ethnography-pseudonyms-altered-details-and-letting-others-check).

### Field safety: write the risk assessment for this trip

- The UK RGS-IBG requires the people it funds to obtain health and safety approval and ethics approval from their own institution before it releases funds[^rgssaferesearch-e1]; the risk assessment must not be a generic template but must be written for the project's location and the nature of the research[^rgssaferesearch-e2].
- The RGS-IBG also asks applicants to think through: could the research offend local cultural taboos? Has appropriate consent been obtained from participants and others affected[^rgssaferesearch-e3]?
- The AAG reminds you that weighing ethical obligations also means considering your own safety, especially if you belong to a marginalized group, or if participants or funders hold power over you[^aag2024ethics-e17].
- The RGS-IBG code says that the level of scrutiny should be proportionate to the risk, and that research with vulnerable or high-risk groups calls for extra care[^rgsgrantscode-e7].

### Positionality and reflexivity: describe the "research instrument" itself

The advice on how to write this section comes mainly from a 2024 short paper by the Finnish scholar Karhulahti. It discusses positionality statements across fields and is not specific to geography; applying it to geographic fieldwork is our own mapping `[Our analysis]`.

**Positionality** is the relationship and position of researchers relative to their research; a **positionality statement** puts it in writing[^karhulahti2024positionality-e1]. **Reflexivity** means thinking, throughout the research, about how your identity, assumptions, and power shape your data and your interpretation `[Our analysis]`.

Why it matters: when the researcher is the "instrument" that produces the primary data (for example, when writing ethnographic field notes), the state of that instrument should be reported[^karhulahti2024positionality-e2]; only a small part of the interactions in the field can be recorded, so who was there and who chose what went into the notes matters[^karhulahti2024positionality-e3]. On the geography side, the AAG statement also asks geographers to reflect on how they represent themselves, participants, and places[^aag2024ethics-e5].

How to write it:

- Include only aspects relevant to this study's methods and topic; don't list identities like a "shopping list"[^karhulahti2024positionality-e4]. For example, if you study an immigrant community, whether you are local and whether you speak the local language may matter more than your other identities `[Our analysis]`.
- Write down your assumptions before you enter the field. Karhulahti sees this as similar to preregistration, since it lets you adjust your analysis early[^karhulahti2024positionality-e5].
- Karhulahti argues that journals should not make positionality statements mandatory, but should use them where they fit the research method[^karhulahti2024positionality-e6]. Whether your target journal wants one is up to that journal `[Our analysis]`.

### Location privacy: coordinates are identifying information

- **Which research needs special care.** Under privacy and confidentiality, the AAG statement lists: automated tracking of the locations and movements of individuals or vehicles; imagery from satellites, drones, and the like at a resolution high enough to identify individuals or vehicles; using high-resolution locations to link data and reveal personal information; and any use of big data that compromises privacy, even when the data are considered "public"[^aag2024ethics-e14].
- **Collect only the precision you need.** The 2026 ethical guidelines on geoprivacy by Malekzadeh and colleagues (authors from Finland, Canada, and elsewhere; the guidelines are advisory) recommend collecting geographic data only when the research question really requires it; a neighborhood-level analysis may not need exact home coordinates[^malekzadeh2026ethical-e2].
- **Tell people in the consent form what can be inferred.** Even if you never ask for an address, home and workplace can often be inferred from repeated GPS traces; tell participants this in plain language[^malekzadeh2026ethical-e3].
- **Removing names is not anonymization.** Distinctive movement patterns such as a daily commute can identify people even after direct identifiers are removed[^malekzadeh2026ethical-e4]. Kwan also warns that if GPS data are mishandled, a person can be identified through reverse geocoding (looking up an address from coordinates)[^kwan2012uncertain-e9].
- **Maps themselves leak information.** Even when the raw data are anonymized, a map can still expose individuals or communities; you can aggregate to coarser levels[^malekzadeh2026ethical-e5], and avoid small-area maps when the findings concern vulnerable or stigmatized groups[^malekzadeh2026ethical-e6]. In a health study mentioned in Kwan's 2012 paper, participants' homes, the places they visited, and their daily paths were never to be printed on maps or displayed publicly[^kwan2012uncertain-e10].
- **Aggregated units can be sensitive too.** Postal code areas and administrative areas can become highly sensitive when they contain few people or are linked to specific health exposures[^malekzadeh2026ethical-e7].
- **Share in tiers.** You can release an aggregated or lower-resolution version publicly and provide the fine-grained version under restricted conditions[^malekzadeh2026ethical-e11]. The AAG also mentions generalizing data or using pseudonyms where needed[^aag2024ethics-e13].
- **"Public online" does not mean consent to research.** Kwan points out that the people who post data such as social media check-ins do not know about, and have not agreed to, their use in research, and there may be no informed consent process at all[^kwan2012uncertain-e11].

The guidelines by Malekzadeh and colleagues list questions stage by stage through a study, which you can use to check yourself before you submit for ethics review[^malekzadeh2026ethical-e9]. These authors observe that many projects are delayed, sent back for revision, or even rejected in ethics review because they did not think through the ethical issues of geographic data[^malekzadeh2026ethical-e10].

### Pitfalls of spatial analysis: change the units, and the conclusion may change

- **The modifiable areal unit problem** (MAUP): when you analyze relationships between variables using data aggregated by area, the results are affected by the size of the areas (the scale effect) and by how their boundaries are drawn (the zoning effect)[^kwan2018limits-e2]. For example, with data from the same city aggregated by neighborhood or by district, the correlation between income and health may come out stronger or weaker `[Our analysis]`. Time has a similar problem: aggregating by day or by month can also lead to different conclusions[^kwan2018limits-e3].
- **The ecological fallacy**: treating a relationship found at the area level as if it held at the individual level. For example, seeing only that "districts with high unemployment also have high crime" does not let you conclude that "unemployed people are more likely to commit crimes"; the people committing crimes in a district are not necessarily the unemployed ones `[Our analysis]`. The guidelines by Malekzadeh and colleagues also remind you to handle the ecological fallacy when using aggregated data[^malekzadeh2026ethical-e8].
- **The uncertain geographic context problem** (UGCoP): a concept Kwan proposed in her 2012 paper of the same name `[Our analysis]`. When you study how the environment affects individuals, you do not know which area actually affects a person, or when and for how long they are exposed to it[^kwan2012uncertain-e3], so conclusions may change with how the "neighborhood" is delineated[^kwan2012uncertain-e2]. For example, different studies have defined the neighborhood as a 1-kilometer or 3-kilometer circle around the home, a 1-kilometer street-network buffer, and so on[^kwan2012uncertain-e5]. Kwan considers this possibly a major reason why studies of environmental effects on health so often reach inconsistent findings[^kwan2012uncertain-e4].
- **A good model fit does not prove you chose the right units.** Kwan points out that the best-fitting model does not necessarily use the true geographic context[^kwan2012uncertain-e7].

What to do: state explicitly which spatial units you used, how close they are to the true geographic context, and which temporal factors you considered[^kwan2012uncertain-e6]; run sensitivity analyses with several scales or zonings and report all of them `[Our analysis]`. Where possible, consider defining the geographic context by a person's **activity space** (the area made up of all the places a person goes to in daily activities and travel[^kwan2012uncertain-e8]) rather than by administrative areas alone `[Our analysis]`.

### Reproducibility and replicability

**Reproducibility** means obtaining consistent results with the same data and procedures; **replicability** means obtaining consistent findings across studies that answer the same question but each collect their own data[^kedron2021reproducibility-e1].

- **Spatial analysis invites specification searching.** Kedron and colleagues (US geographic information scientists) point out that parameters such as the scale and the definition of "neighboring" must be fixed in advance, yet researchers often do not know their true values, which widens the range of "reasonable specifications" they might explore[^kedron2021reproducibility-e2]. Their example: a spatial regression study of urbanization and air quality must choose a spatial weights matrix (which cities count as neighbors); if many are tried and only one is reported, the other tests disappear from the literature[^kedron2021reproducibility-e3]. They suggest that a pre-analysis plan for geographic research state the scale of analysis and the spatial weights matrices to be examined[^kedron2021reproducibility-e4], but acknowledge that the geospatial community has yet to explore preregistration in depth[^kedron2021reproducibility-e5].
- **Explain how concepts became spatial data.** To reproduce a geographic study, you need to know how the spatial processes were conceptualized, measured, and operationalized in the analysis[^kedron2021reproducibility-e13].
- **Failing to hold elsewhere is not necessarily failure.** How much a change in location, time, or context has to differ before you should stop expecting a result to replicate is still unsettled[^kedron2021reproducibility-e6]; Kedron and colleagues suggest seeing replicability as a spectrum[^kedron2021reproducibility-e7].
- **One small assessment was not encouraging.** In 2018, Nüst and colleagues assessed only 32 papers from one European GIScience conference (AGILE), all nominated for best paper in 2010 and 2012–2017[^nust2018reproducible-e3]. None reached the highest level of reproducibility in any category; for 19 of the 32, the data were neither available nor re-creatable from the paper[^nust2018reproducible-e4]. Of the 82 authors of these 32 papers, 22 answered a survey, and the reasons they cited most often were legal restrictions and lack of time[^nust2018reproducible-e6][^nust2018reproducible-e7]. Nüst and colleagues also argue that proprietary (commercial, closed-source) software will ultimately be a fatal barrier to reproducibility[^nust2018reproducible-e9]. The sample is small and represents only this conference's nominated papers, not geography as a whole `[Our analysis]`.
- **When the data cannot be made public.** Geographic data involving people often cannot be shared[^kedron2021reproducibility-e8]. You can release the code along with a simulated dataset that preserves the spatial structure of the original data[^kedron2021reproducibility-e9]; Kedron and colleagues also argue that such research should not be kept out of publication because of this[^kedron2021reproducibility-e11].
- **Qualitative research can leave a record too.** Interview information and the process of coding and extracting themes can be recorded, just like computational steps[^kedron2021reproducibility-e12]. How transparent ethnography should be is still debated; some propose compromises such as partial disclosure of people or places and sharing coding schemes[^jerolmack2024ethnography-e5]. See the [Sociology page](../sociology/README.md#transparency-in-qualitative-research-the-debate-continues) for details.

For general practice in organizing data and code, see [Organizing your research materials](../../08_throughout/organizing_materials.md) in Throughout the project.

---

## Common strategies and standards of evidence

A **research strategy** is the main logic by which a project produces new knowledge; see [Key concepts](../../00_start-here/key-concepts.md#research-strategy) and [Research strategies](../../05_research-strategies/README.md). The table below lists only the strategies this page's sources support. The grouping and summaries are our own, and each standard represents only the author or society cited in its footnote `[Our analysis]`.

| Strategy | What it looks like in geography | Common evidence and standards | How to do it |
|---|---|---|---|
| [Description](../../05_research-strategies/observe_describe.md) (quantitative) | Use location data to describe how a phenomenon is distributed in space | Conclusions from area data change with scale and zoning[^kwan2018limits-e2]; explain how spatial processes were conceptualized, measured, and operationalized[^kedron2021reproducibility-e13]; a pre-analysis plan states the scale of analysis and the spatial weights matrices to be examined[^kedron2021reproducibility-e4] | [Spatial analysis](practices/spatial_analysis.md) |
| [Causal explanation](../../05_research-strategies/explain_causality.md) | Study how the environment affects individuals, for example the effects of the social and physical environment on health[^kwan2012uncertain-e4] | State which spatial units you used, how close they are to the true geographic context, and which temporal factors you considered[^kwan2012uncertain-e6]; the best-fitting model does not necessarily use the true geographic context[^kwan2012uncertain-e7]; handle the ecological fallacy when using aggregated data[^malekzadeh2026ethical-e8] | [Spatial analysis](practices/spatial_analysis.md), [Mixed methods](../../06_methods/mixed_methods.md) |
| [Description](../../05_research-strategies/observe_describe.md) (qualitative fieldwork) | Go to a place for interviews, participant observation, and participatory mapping to understand the relationship between people and place; the AAG values doing research "with" participants[^aag2024ethics-e4] | When the researcher is the "instrument" producing the data, report your positionality[^karhulahti2024positionality-e2]; reflect on how you represent yourself, participants, and places[^aag2024ethics-e5]; the process of interviewing, coding, and extracting themes can also be recorded[^kedron2021reproducibility-e12] | [Interview studies](../../06_methods/interview_study.md), [Case study and ethnography](../../06_methods/case_study.md) |

How to use this table `[Our analysis]`: first find your strategy from your central claim. Quantitative and qualitative work are often combined: for example, adding qualitative information on how people perceive their environment when measuring environmental exposure seems to help mitigate the uncertain geographic context problem[^kwan2018limits-e4].

## Research methods common in this field

**Specific to this field**: [Spatial analysis](practices/spatial_analysis.md). Other methods and the corresponding pages among the cross-field research types are listed below (the correspondences and the notes on differences are our own summary `[Our analysis]`; the footnotes give the basis). For fieldwork in physical geography, see [Field studies: observation and sampling](../../06_methods/field_study.md).

- **In-depth interviews, ethnography, and case studies of places**: see [Interview studies](../../06_methods/interview_study.md) and [Case study and ethnography](../../06_methods/case_study.md). Differences: you need to report your positionality (see "Positionality and reflexivity" above); when quoting, watch whether place details could identify an interviewee[^aag2024ethics-e13]; the case is often a "place," and the work may involve fieldwork abroad, in which case projects funded by the UK RGS-IBG must also pass review in the host country[^rgsgrantscode-e3].
- **GPS and mobility trajectory studies**: for how to do them, see [Spatial analysis](practices/spatial_analysis.md); they carry the highest privacy risk, see "Location privacy" above[^malekzadeh2026ethical-e4].
- **Questionnaire surveys**: see [Questionnaire surveys](../../06_methods/questionnaire_survey.md). Difference: addresses and frequently visited places in a questionnaire are sensitive information in themselves, so collect only the precision you need[^malekzadeh2026ethical-e2].
- **Mixed methods and replication studies**: see [Mixed methods](../../06_methods/mixed_methods.md) and [Replication studies](../../06_methods/replication.md). Difference: first decide whether you should expect "reproduction" or "replication elsewhere"[^kedron2021reproducibility-e6].

---

## Advice for newcomers

1. **Decide the spatial precision of your data before you write the consent form.** Ask yourself how precise a location you really need to answer the research question. Enough is enough[^malekzadeh2026ethical-e2]; and say in the consent form what can be inferred from these data[^malekzadeh2026ethical-e3].
2. **Use open-source tools where you can, and write your analysis as scripts** `[Our analysis]`. Nüst and colleagues consider proprietary software a fatal barrier to reproducibility[^nust2018reproducible-e9]; in their assessment, "data available on request" also counted as unavailable[^nust2018reproducible-e5].
3. **Write a short positionality reflection before you enter the field.** Include only the identities and assumptions relevant to this study[^karhulahti2024positionality-e4], and add to it as fieldwork goes on `[Our analysis]`.
4. **If you do fieldwork abroad, check the host country's ethics review and safety requirements early.** The UK RGS-IBG's requirements for the projects it funds are a useful reference: write the risk assessment for the specific location[^rgssaferesearch-e2], and apply to the host country's ethics committee if there is one[^rgsgrantscode-e3]; in the end, follow the rules of your institution and your funder `[Our analysis]`.
5. **Before publishing, check every map as you would check data.** Ask: could someone use this map to find a participant's home[^malekzadeh2026ethical-e5]?
6. **Take the results back to local people.** Use a form they can understand[^aag2024ethics-e12], and agree on authorship with local collaborators at the start[^aag2024ethics-e8][^rgsgrantscode-e5].

---

## Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Analyzing with only one kind of spatial unit (such as administrative districts) without giving a reason | Results change with scale and zoning[^kwan2018limits-e2]; inconsistent findings across similar studies may come down to different units[^kwan2012uncertain-e4] |
| Drawing conclusions about individuals from area-level aggregated data | This is the ecological fallacy: a relationship at the area level cannot be applied directly to individuals `[Our analysis]`[^malekzadeh2026ethical-e8] |
| Assuming GPS tracks are anonymous once names are removed | Distinctive movement patterns can identify people on their own[^malekzadeh2026ethical-e4][^malekzadeh2026ethical-e1] |
| Putting point maps of participants' homes or daily paths in the paper | The map itself exposes individuals[^malekzadeh2026ethical-e5]; some studies explicitly forbid such maps[^kwan2012uncertain-e10] |
| Treating social media check-ins as "public" and free to use | The AAG warns that data considered public can still compromise privacy[^aag2024ethics-e14]; the people who posted them did not agree to be studied[^kwan2012uncertain-e11] |
| Ignoring the host country's ethics review because your own institution approved the project | The UK RGS-IBG requires the projects it funds to get approval from the host country's ethics committee where one exists[^rgsgrantscode-e3] |
| Writing the field risk assessment from a template | The RGS-IBG requires applicants to write it for the specific location and nature of the research[^rgssaferesearch-e2] |
| Leaving when fieldwork ends without giving anything back locally | The AAG requires that, where appropriate, results be shared in a form people can understand[^aag2024ethics-e12]; the RGS-IBG code requires local people to be involved through to feedback after the research[^rgsgrantscode-e4] |

---

## Further reading

- **AAG Statement of Professional Ethics (revised 2024)**: the American Association of Geographers' ethics statement for its members, with specific provisions on fieldwork, consent, geospatial technologies and privacy, and funding disclosure. Read it before you start research involving people or places.
- **RGS-IBG Code of Practice for the Grants Programme and its safety and ethics guidance**: the Royal Geographical Society's rules for the projects it funds. Short; covers host-country review, local collaborators, the rationale for travel, and risk assessment. Read it when you prepare for fieldwork abroad.
- **Kwan 2012, The Uncertain Geographic Context Problem**, and **Kwan 2018, The Limits of the Neighborhood Effect**: make clear how spatial units and geographic context shape conclusions (full texts on the author's homepage). Read them before neighborhood-effect or environmental-exposure studies.
- **Kedron et al. 2021, Reproducibility and replicability: opportunities and challenges for geospatial research**: why geographic research is prone to specification searching, what a pre-analysis plan should contain, and what to do when data cannot be shared.
- **Nüst et al. 2018, Reproducible research and GIScience**: an assessment of the reproducibility of 32 AGILE conference papers, with concrete recommendations for authors (open access).
- **Malekzadeh et al. 2026, Ethical guidelines for geoprivacy**: geoprivacy self-check questions organized by research stage (open access). Go through them one by one before you write your ethics application.
- **Karhulahti 2024, Positionality statements in science**: a short cross-disciplinary paper on what positionality statements are for and how to write them so they are not a mere formality (open access).

[^aag2024ethics-e1]: AAG Statement of Professional Ethics (2024), I. Preamble. [Evidence](../../../sources/notes/aag2024ethics.md#e1)
[^aag2024ethics-e2]: AAG Statement of Professional Ethics, I. Preamble. [Evidence](../../../sources/notes/aag2024ethics.md#e2)
[^aag2024ethics-e3]: AAG Statement of Professional Ethics, II. Do Good. [Evidence](../../../sources/notes/aag2024ethics.md#e3)
[^aag2024ethics-e4]: AAG Statement of Professional Ethics, II. Respect Research Participants. [Evidence](../../../sources/notes/aag2024ethics.md#e4)
[^aag2024ethics-e5]: AAG Statement of Professional Ethics, II. Respect Research Participants. [Evidence](../../../sources/notes/aag2024ethics.md#e5)
[^aag2024ethics-e6]: AAG Statement of Professional Ethics, III. Do No Harm. [Evidence](../../../sources/notes/aag2024ethics.md#e6)
[^aag2024ethics-e7]: AAG Statement of Professional Ethics, III. Recognize Power Hierarchies. [Evidence](../../../sources/notes/aag2024ethics.md#e7)
[^aag2024ethics-e8]: AAG Statement of Professional Ethics, IV. Collaborate with Care. [Evidence](../../../sources/notes/aag2024ethics.md#e8)
[^aag2024ethics-e9]: AAG Statement of Professional Ethics, VI. Obtain Informed Consent. [Evidence](../../../sources/notes/aag2024ethics.md#e9)
[^aag2024ethics-e10]: AAG Statement of Professional Ethics, VI. Obtain Institutional Approval. [Evidence](../../../sources/notes/aag2024ethics.md#e10)
[^aag2024ethics-e11]: AAG Statement of Professional Ethics, VI. Take Informed Consent Seriously. [Evidence](../../../sources/notes/aag2024ethics.md#e11)
[^aag2024ethics-e12]: AAG Statement of Professional Ethics, VI. Share Findings. [Evidence](../../../sources/notes/aag2024ethics.md#e12)
[^aag2024ethics-e13]: AAG Statement of Professional Ethics, VI. Make Data Available. [Evidence](../../../sources/notes/aag2024ethics.md#e13)
[^aag2024ethics-e14]: AAG Statement of Professional Ethics, VI. Protect Privacy and Confidentiality. [Evidence](../../../sources/notes/aag2024ethics.md#e14)
[^aag2024ethics-e15]: AAG Statement of Professional Ethics, VII. Disclose Funding Sources. [Evidence](../../../sources/notes/aag2024ethics.md#e15)
[^aag2024ethics-e16]: AAG Statement of Professional Ethics, VII. Be Transparent. [Evidence](../../../sources/notes/aag2024ethics.md#e16)
[^aag2024ethics-e17]: AAG Statement of Professional Ethics, VIII. Weigh Competing Ethical Obligations. [Evidence](../../../sources/notes/aag2024ethics.md#e17)
[^aag2024ethics-e18]: AAG Statement of Professional Ethics, revision history at the top of the page. [Evidence](../../../sources/notes/aag2024ethics.md#e18)
[^rgsgrantscode-e1]: RGS-IBG Code of Practice for the Grants Programme, start of the ethics clause. [Evidence](../../../sources/notes/rgsgrantscode.md#e1)
[^rgsgrantscode-e3]: RGS-IBG Code of Practice for the Grants Programme, ethics clause. [Evidence](../../../sources/notes/rgsgrantscode.md#e3)
[^rgsgrantscode-e4]: RGS-IBG Code of Practice for the Grants Programme, ethics clause. [Evidence](../../../sources/notes/rgsgrantscode.md#e4)
[^rgsgrantscode-e5]: RGS-IBG Code of Practice for the Grants Programme, ethics clause. [Evidence](../../../sources/notes/rgsgrantscode.md#e5)
[^rgsgrantscode-e6]: RGS-IBG Code of Practice for the Grants Programme, sustainable research clause. [Evidence](../../../sources/notes/rgsgrantscode.md#e6)
[^rgsgrantscode-e7]: RGS-IBG Code of Practice for the Grants Programme, ethics clause. [Evidence](../../../sources/notes/rgsgrantscode.md#e7)
[^rgssaferesearch-e1]: RGS-IBG, Safe, responsible and ethical research, opening section. [Evidence](../../../sources/notes/rgssaferesearch.md#e1)
[^rgssaferesearch-e2]: RGS-IBG, Safe, responsible and ethical research, risk assessment paragraph. [Evidence](../../../sources/notes/rgssaferesearch.md#e2)
[^rgssaferesearch-e3]: RGS-IBG, Safe, responsible and ethical research, ethics assessment paragraph. [Evidence](../../../sources/notes/rgssaferesearch.md#e3)
[^karhulahti2024positionality-e1]: Karhulahti 2024, Introduction. [Evidence](../../../sources/notes/karhulahti2024positionality.md#e1)
[^karhulahti2024positionality-e2]: Karhulahti 2024, What positionality does. [Evidence](../../../sources/notes/karhulahti2024positionality.md#e2)
[^karhulahti2024positionality-e3]: Karhulahti 2024, What positionality does. [Evidence](../../../sources/notes/karhulahti2024positionality.md#e3)
[^karhulahti2024positionality-e4]: Karhulahti 2024, Two common misunderstandings. [Evidence](../../../sources/notes/karhulahti2024positionality.md#e4)
[^karhulahti2024positionality-e5]: Karhulahti 2024, What positionality does. [Evidence](../../../sources/notes/karhulahti2024positionality.md#e5)
[^karhulahti2024positionality-e6]: Karhulahti 2024, Two common misunderstandings. [Evidence](../../../sources/notes/karhulahti2024positionality.md#e6)
[^malekzadeh2026ethical-e1]: Malekzadeh et al. 2026, Introduction. [Evidence](../../../sources/notes/malekzadeh2026ethical.md#e1)
[^malekzadeh2026ethical-e2]: Malekzadeh et al. 2026, Data collection, Q2. [Evidence](../../../sources/notes/malekzadeh2026ethical.md#e2)
[^malekzadeh2026ethical-e3]: Malekzadeh et al. 2026, Data collection, Q4. [Evidence](../../../sources/notes/malekzadeh2026ethical.md#e3)
[^malekzadeh2026ethical-e4]: Malekzadeh et al. 2026, Q24. [Evidence](../../../sources/notes/malekzadeh2026ethical.md#e4)
[^malekzadeh2026ethical-e5]: Malekzadeh et al. 2026, Results dissemination, Q59. [Evidence](../../../sources/notes/malekzadeh2026ethical.md#e5)
[^malekzadeh2026ethical-e6]: Malekzadeh et al. 2026, Results dissemination, Q59. [Evidence](../../../sources/notes/malekzadeh2026ethical.md#e6)
[^malekzadeh2026ethical-e7]: Malekzadeh et al. 2026, introduction to the Ethical questions section. [Evidence](../../../sources/notes/malekzadeh2026ethical.md#e7)
[^malekzadeh2026ethical-e8]: Malekzadeh et al. 2026, Data analysis, Q53. [Evidence](../../../sources/notes/malekzadeh2026ethical.md#e8)
[^malekzadeh2026ethical-e9]: Malekzadeh et al. 2026, Ethical questions for geographic data privacy in research. [Evidence](../../../sources/notes/malekzadeh2026ethical.md#e9)
[^malekzadeh2026ethical-e10]: Malekzadeh et al. 2026, Introduction. [Evidence](../../../sources/notes/malekzadeh2026ethical.md#e10)
[^malekzadeh2026ethical-e11]: Malekzadeh et al. 2026, Data sharing, Q34. [Evidence](../../../sources/notes/malekzadeh2026ethical.md#e11)
[^kwan2012uncertain-e2]: Kwan 2012, p. 959. [Evidence](../../../sources/notes/kwan2012uncertain.md#e2)
[^kwan2012uncertain-e3]: Kwan 2012, p. 959. [Evidence](../../../sources/notes/kwan2012uncertain.md#e3)
[^kwan2012uncertain-e4]: Kwan 2012, p. 959. [Evidence](../../../sources/notes/kwan2012uncertain.md#e4)
[^kwan2012uncertain-e5]: Kwan 2012, p. 960. [Evidence](../../../sources/notes/kwan2012uncertain.md#e5)
[^kwan2012uncertain-e6]: Kwan 2012, p. 963. [Evidence](../../../sources/notes/kwan2012uncertain.md#e6)
[^kwan2012uncertain-e7]: Kwan 2012, pp. 963–964. [Evidence](../../../sources/notes/kwan2012uncertain.md#e7)
[^kwan2012uncertain-e8]: Kwan 2012, p. 964. [Evidence](../../../sources/notes/kwan2012uncertain.md#e8)
[^kwan2012uncertain-e9]: Kwan 2012, p. 966, note 2. [Evidence](../../../sources/notes/kwan2012uncertain.md#e9)
[^kwan2012uncertain-e10]: Kwan 2012, p. 966, note 2. [Evidence](../../../sources/notes/kwan2012uncertain.md#e10)
[^kwan2012uncertain-e11]: Kwan 2012, p. 966, note 2. [Evidence](../../../sources/notes/kwan2012uncertain.md#e11)
[^kwan2018limits-e2]: Kwan 2018, p. 1486. [Evidence](../../../sources/notes/kwan2018limits.md#e2)
[^kwan2018limits-e3]: Kwan 2018, p. 1486. [Evidence](../../../sources/notes/kwan2018limits.md#e3)
[^kwan2018limits-e4]: Kwan 2018, p. 1488. [Evidence](../../../sources/notes/kwan2018limits.md#e4)
[^kedron2021reproducibility-e1]: Kedron et al. 2021, §1 Introduction. [Evidence](../../../sources/notes/kedron2021reproducibility.md#e1)
[^kedron2021reproducibility-e2]: Kedron et al. 2021, §2. [Evidence](../../../sources/notes/kedron2021reproducibility.md#e2)
[^kedron2021reproducibility-e3]: Kedron et al. 2021, §2. [Evidence](../../../sources/notes/kedron2021reproducibility.md#e3)
[^kedron2021reproducibility-e4]: Kedron et al. 2021, §3.1. [Evidence](../../../sources/notes/kedron2021reproducibility.md#e4)
[^kedron2021reproducibility-e5]: Kedron et al. 2021, §3.1. [Evidence](../../../sources/notes/kedron2021reproducibility.md#e5)
[^kedron2021reproducibility-e6]: Kedron et al. 2021, §4.1. [Evidence](../../../sources/notes/kedron2021reproducibility.md#e6)
[^kedron2021reproducibility-e7]: Kedron et al. 2021, §4.1. [Evidence](../../../sources/notes/kedron2021reproducibility.md#e7)
[^kedron2021reproducibility-e8]: Kedron et al. 2021, §3.2. [Evidence](../../../sources/notes/kedron2021reproducibility.md#e8)
[^kedron2021reproducibility-e9]: Kedron et al. 2021, §3.2. [Evidence](../../../sources/notes/kedron2021reproducibility.md#e9)
[^kedron2021reproducibility-e10]: Kedron et al. 2021, §3.2. [Evidence](../../../sources/notes/kedron2021reproducibility.md#e10)
[^kedron2021reproducibility-e11]: Kedron et al. 2021, §3.2. [Evidence](../../../sources/notes/kedron2021reproducibility.md#e11)
[^kedron2021reproducibility-e12]: Kedron et al. 2021, §3.1. [Evidence](../../../sources/notes/kedron2021reproducibility.md#e12)
[^kedron2021reproducibility-e13]: Kedron et al. 2021, §4.2. [Evidence](../../../sources/notes/kedron2021reproducibility.md#e13)
[^nust2018reproducible-e1]: Nüst et al. 2018, Introduction. [Evidence](../../../sources/notes/nust2018reproducible.md#e1)
[^nust2018reproducible-e2]: Nüst et al. 2018, Materials & Methods. [Evidence](../../../sources/notes/nust2018reproducible.md#e2)
[^nust2018reproducible-e3]: Nüst et al. 2018, Materials & Methods. [Evidence](../../../sources/notes/nust2018reproducible.md#e3)
[^nust2018reproducible-e4]: Nüst et al. 2018, Results. [Evidence](../../../sources/notes/nust2018reproducible.md#e4)
[^nust2018reproducible-e5]: Nüst et al. 2018, Materials & Methods, Definition and criteria. [Evidence](../../../sources/notes/nust2018reproducible.md#e5)
[^nust2018reproducible-e6]: Nüst et al. 2018, Results, Author feedback. [Evidence](../../../sources/notes/nust2018reproducible.md#e6)
[^nust2018reproducible-e7]: Nüst et al. 2018, Results, Author feedback. [Evidence](../../../sources/notes/nust2018reproducible.md#e7)
[^nust2018reproducible-e9]: Nüst et al. 2018, Discussion, Suggestions to authors. [Evidence](../../../sources/notes/nust2018reproducible.md#e9)
[^jerolmack2024ethnography-e5]: Jerolmack, Murphy & Reyes 2024, paragraph 2. [Evidence](../../../sources/notes/jerolmack2024ethnography.md#e5)
