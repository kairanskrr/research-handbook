# Pebesma & Bivand 2023: Spatial Data Science: With Applications in R

- Source: `pebesma2023spatial`, [free online version](https://r-spatial.org/book/)
- Version: Textbook published by CRC Press in 2023; the authors make the full text freely available online. The authors are lead developers of R packages for spatial data (sf, stars, spdep, etc.). We read chapter 2, Coordinates, and chapter 5, Attributes and Support, of the online version. Locations give chapters and sections.

### E1

- Location: Chapter 2, Coordinates, section 2.3
- Quote: "The definitions above imply that coordinates in degrees longitude and latitude only have a meaning and can only be interpreted unambiguously as Earth coordinates, when the datum they are associated with is given."
- Key point: Longitude and latitude coordinates have an unambiguous meaning only when the datum they refer to is given.

### E2

- Location: Chapter 2, Coordinates, section on projected coordinates
- Quote: "Projecting ellipsoidal coordinates means that shapes, directions, areas, or even all three, are distorted"
- Key point: Projecting coordinates from the Earth onto a plane distorts at least one of shape, direction, or area.

### E3

- Location: Chapter 2, Coordinates, section 2.3
- Quote: "Recomputing coordinates in a new datum is called coordinate transformation, and is approximate: because datums are a result of model fitting, transformations between datums are models too that have been fit"
- Key point: Converting coordinates between datums (coordinate transformation) is approximate and carries its own error.

### E4

- Location: Chapter 2, Coordinates, section on PROJ
- Quote: "Where we could safely assume for many decades that spatial data with ellipsoidal coordinates would have axis order (longitude, latitude), this is no longer the case."
- Key point: You can no longer assume that latitude/longitude data come in the axis order (longitude, latitude).

### E5

- Location: Chapter 5, Attributes and Support, introduction
- Quote: "for non-point geometries (lines, polygons), feature attribute values either have point support, meaning that the value applies to every point, or they have block support, meaning that the value summarises all points in the geometry."
- Key point: Attribute values on lines and polygons either hold for every point within them (point support) or summarize the whole area (block support).

### E6

- Location: Chapter 5, Attributes and Support, introduction
- Quote: "The reason for this is that the dataset contains variables with values that are associated with entire polygons – in this case population counts – meaning they are not associated with a POINT geometry replacing the polygon."
- Key point: Example: when county polygons are replaced by their centroids, values that belong to the whole polygon, such as population counts, do not belong to the point, and the software issues a warning.

### E7

- Location: Chapter 5, Attributes and Support, section 5.2
- Quote: "Properly specifying attribute-geometry relationships, and warning against their absence or cases when change in geometry (change of support) implies a change of information can help to avoid a large class of common spatial data analysis mistakes"
- Key point: Specifying attribute-geometry relationships, and warning when a change of geometry (change of support) implies a change of information, helps avoid a large class of common spatial analysis errors.

### E8

- Location: Chapter 5, Attributes and Support, section on spatial aggregation
- Quote: "When we need an aggregate for a new area that is not a union of the geometries for a group of records, and we use a spatial predicate, then single records may be matched to multiple groups."
- Key point: When aggregating to a different set of boundaries using a spatial predicate (e.g., "intersects"), a single record may be matched to several areas and counted more than once.

### E9

- Location: Chapter 5, Attributes and Support, section on spatial aggregation
- Quote: "If points fall on a shared boundary than they are assigned to both polygons"
- Key point: Points lying exactly on a shared boundary are assigned to both polygons.

### E10

- Location: Chapter 5, Attributes and Support, section on area-weighted interpolation
- Quote: "Extensive variables correspond to amounts, associated with a physical size (length, area, volume, counts of items). An example of a extensive variable is population count." / "An example of a related variable that is intensive is population density."
- Key point: Extensive variables are amounts (e.g., population count) that must be split when areas are split; intensive variables are ratios (e.g., population density) that cannot be summed after splitting.

### E11

- Location: Chapter 5, Attributes and Support, section 5.4 (upscaling and downscaling)
- Quote: "Of course this makes only sense to the extent that the assumptions hold: over the source regions extensive variables need to be uniformly distributed and intensive variables need to have a constant value."
- Key point: Area-weighted interpolation only makes sense if its assumptions hold: extensive variables are uniformly distributed over the source regions, and intensive variables are constant across them.
