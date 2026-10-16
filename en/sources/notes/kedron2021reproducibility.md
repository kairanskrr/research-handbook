# Kedron et al. 2021: Reproducibility and replicability: opportunities and challenges for geospatial research

- Source: `kedron2021reproducibility`, [original PDF (US National Science Foundation public access repository)](https://par.nsf.gov/servlets/purl/10292882), doi:10.1080/13658816.2020.1802032
- Version: Review article in the International Journal of Geographical Information Science (IJGIS), published online August 2020 and in print in 2021 (vol. 35, no. 3). The authors are geographic information science scholars at Arizona State University and the University of California, Santa Barbara. We read the publisher's version PDF from the US National Science Foundation (NSF) public access repository. Locations give sections.

### E1

- Location: §1 Introduction
- Quote: "Reproducibility – obtaining results consistent with a prior study using the same materials, procedures, and conditions of analysis – and Replicability – obtaining consistent findings across studies that aim to answer the same question but with each study collecting and using its own data"
- Key point: Reproducibility means obtaining results consistent with a prior study using the same materials, procedures, and conditions of analysis; replicability means obtaining consistent findings across studies that answer the same question but each collect their own data.

### E2

- Location: §2
- Quote: "Geospatial research is susceptible to specification search because spatial analyses require a well-documented set of apriori decisions that set the parameters of analysis (e.g. the scale of analysis, representation of spatial relationships). [...] This lack of knowledge widens the range of reasonable specifications a researcher might explore."
- Key point: Spatial analysis requires a set of a priori decisions that fix its parameters (e.g., the scale of analysis, how spatial relationships are represented), and researchers often do not know the true values of these parameters, so there are even more "reasonable" specifications to choose from; this makes geospatial research susceptible to specification search (trying many specifications and reporting only one).

### E3

- Location: §2
- Quote: "they also needed to choose a weight matrix that defines the spatial relationships that exist among neighboring cities [...] If only one of these many spatial regression specifications is reported, these many other tests are not included in the literature and cannot be replicated or reproduced."
- Key point: Example: a study of urbanization and air quality in 289 Chinese cities also had to choose a spatial weight matrix for its spatial regression (defining which cities count as "neighbors"); if many specifications are tried and only one reported, the other tests vanish from the literature and others cannot reproduce or replicate the work.

### E4

- Location: §3.1
- Quote: "a geographic pre-analysis plan would likely need to include an explicit statement of the scale(s) used in the analysis [...] research using spatial statistical methods to explore or adjust for the impacts of spatial autocorrelation would need to outline and justify the range of spatial weights matrices examined."
- Key point: A geographic pre-analysis plan would likely need to state the scale(s) of analysis explicitly; studies using spatial statistical methods would need to list and justify the spatial weight matrices they will test.

### E5

- Location: §3.1
- Quote: "To our knowledge, the geospatial community has yet to deeply explore the possibilities of pre-analysis plans and pre-registration or the practicalities of their implementation."
- Key point: To the authors' knowledge, the geospatial community has yet to deeply explore pre-analysis plans and preregistration or how to implement them in practice.

### E6

- Location: §4.1
- Quote: "While it may be reasonable to expect geospatial analysis to be reproducible, it is less clear whether or not geospatial research should be replicable. When does a change in the location, time, or context of a second study represent enough of a difference that we should no longer expect a result to replicate?"
- Key point: Expecting geospatial analysis to be reproducible is reasonable, but it is less clear whether it should be expected to replicate: how much change in location, time, or context is enough that the results should no longer be expected to recur?

### E7

- Location: §4.1
- Quote: "It may also be useful for GIScience to develop an assessment framework for individual studies that recognize replicability not as a binary success-failure measure, but as existing along a spectrum."
- Key point: The authors suggest treating replicability as a spectrum rather than a binary success-or-failure measure.

### E8

- Location: §3.2
- Quote: "Geospatial analyses involving human subjects often requires that collected data not only be anonymized but that data also not be shared to preserve confidentiality."
- Key point: Geospatial analyses involving human subjects often require not only anonymizing the data but also not sharing them, to preserve confidentiality.

### E9

- Location: §3.2
- Quote: "Shepherd et al. (2017) propose that researchers release the code used in an analysis, but rather than releasing the original data, create and release a simulated dataset with characteristics that match the original data [...] In geospatial research, such simulated data could be created to match the spatial structures (e.g. autocorrelation) and attribute relationships in the original data."
- Key point: When data cannot be made public, one option is to release the code along with a simulated dataset that matches the original data's characteristics; in geographic research, simulated data can preserve the original's spatial structure (such as spatial autocorrelation) and attribute relationships.

### E10

- Location: §3.2
- Quote: "this journal has a data-sharing policy that requires authors to make data and research artifacts freely available and aligned with FAIR standards."
- Key point: IJGIS has a data-sharing policy requiring authors to make data and research artifacts freely available and aligned with the FAIR principles (findable, accessible, interoperable, reusable).

### E11

- Location: §3.2
- Quote: "If a geospatial researcher cannot share data for ethical reasons or because an industry partner is restricting the release of data, that research should not be kept from the published record."
- Key point: Research whose data cannot be shared for ethical reasons or because of restrictions from an industry partner should not be kept out of the published record.

### E12

- Location: §3.1
- Quote: "Interview information could be similarly recorded, as could information about the process of coding and theme extraction common in many qualitative studies."
- Key point: Interview information, and the process of coding and theme extraction in qualitative research, can be recorded just like computational steps.

### E13

- Location: §4.2
- Quote: "In geospatial research, the details necessary for reproduction include information about how spatial processes were conceptualized, measured through spatial data, and then operationalized during analysis."
- Key point: To be reproducible, geospatial research must explain how spatial processes were conceptualized, measured through spatial data, and operationalized in the analysis.
