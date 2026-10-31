import sys
from netin.models import PATCHModel, CompoundLFM

import time

def run():
    print("time_us,n,m,fn",file=sys.stderr)
    n = 10000
    for n in [1000,10000,100000]:
        k = 3
        f_m = 0.2
        h_MM = 0.5
        h_mm = 0.5
        tau = 0.3
        lfm_l = CompoundLFM.PAH
        lfm_g = CompoundLFM.PAH
        seed = 1234
        for i in range(11):
            start = time.perf_counter_ns()
            model = PATCHModel(n=n, k=k, f_m=f_m,
                               tau=tau,
                               lfm_tc=lfm_l, lfm_global=lfm_g,
                               h_mm=h_mm, h_MM=h_MM,
                               seed=seed)
            model.simulate()
            elapsed = int((time.perf_counter_ns() - start) / 1000);
            if i != 0:
                print(f"{elapsed},{model.graph.number_of_nodes()},{model.graph.number_of_edges()},original",file=sys.stderr)



if __name__ == '__main__':
    run()
