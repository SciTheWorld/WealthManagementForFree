/**
 * Created by jose on 19/09/16.
 */

import { Holding } from  '../../shared/model/holding';

export class HoldingsService {
    private total: number = 23434;
    private benefit: number  = 150;
    private portfolio: Holding[] = [new Holding('IBM',23), new Holding('SAN',12)];


    getTotal() {
        return this.total;
    }

    getBenefit() {
        return this.benefit;
    }

    getPortfolio(name: string) {
        return this.portfolio;

    }

    getPrices() {
       return [{'IBM':155.86, 'SAN':23}];
    }
}
