# CS596FinalProject

Based on a hybrid MPI+OpenMP parallel molecular dynamics (MD) program, optimizing the performance of the hybrid MPI+OpenMP MD code. Methonds takedn into consideration: 1. enclose the entire MD loop in a parallel clause in the main function to avoid the excessive fork-join overhead. 2. use a lock variable for synchronization.
