# # DAILY CODE MODE
# def reverse(N, A):
#     return(A[:N][::-1] + A[N:])
#
# reverse(4, [1,2,3,4,5])
#
# # Answer by Ttl
# reverse = lambda n,a:a[:n][::-1]+a[n:]
#
# # BREAKDOWN
# lambda n,a:a[:n][::-1]+a[n:]
#
# if we take my answer and bump it up to one line and then compare it to the answer we can see that really what is happening is that lambdas do not need to be declared and that that they have to return a value.
# def reverse(N, A): return(A[:N][::-1] + A[N:])
# lambda n,a:a[:n][::-1]+a[n:]
#
# SUMMARY
# Identical answers.