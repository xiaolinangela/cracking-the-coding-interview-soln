# Divide the file into chunks, whcih are x megabytes each, where x is the amount of memory we have available. Each chunk is sorted separately and then saved back to the file system.
# Once all the chunks are sorted, we merge the chunks, one by one. At the end, we have a full sorted file. This algorithm is know as external sort.
