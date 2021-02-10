#Filter homelessness for cases where the number of individuals is greater than ten thousand, assigning to ind_gt_10k. View the printed result.

# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness["individuals"] > 10000]

# See the result
print(ind_gt_10k)


#Filter homelessness for cases where the USA Census region is "Mountain", assigning to mountain_reg. View the printed result.

# Filter for rows where region is Mountain
mountain_reg = homelessness[homelessness["region"] == "Mountain"]

# See the result
print(mountain_reg)


#Filter homelessness for cases where the number of family_members is less than one thousand and the region is "Pacific",
#assigning to fam_lt_1k_pac. View the printed result.

# Filter for rows where family_members is less than 1000 
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness["family_members"] < 1000) 
& (homelessness["region"] == "Pacific")]
# See the result
print(fam_lt_1k_pac)
