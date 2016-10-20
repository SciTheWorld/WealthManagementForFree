import {Component, Injectable, OnInit} from '@angular/core';
import {HoldingsService} from './holdings.service';
import {Holding} from '../../shared/model/holding';

@Component({
    moduleId: module.id,
    selector: 'robot-holdings-man-data',
    templateUrl: './holdingsMD.component.html',
    providers: [HoldingsService]
})

@Injectable()
export class HoldingsMDComponent implements OnInit {
    total:number;
    benefit: number ;
    portfolio: Holding[];
    prices: any;

    constructor(private holdingService: HoldingsService) {}

    ngOnInit(): void {
        this.total = this.holdingService.getTotal();
        this.benefit = this.holdingService.getBenefit();
        this.portfolio = this.holdingService.getPortfolio('user');
        this.prices = this.holdingService.getPrices();
    }

    getPrice(share: string) {
        return(this.prices[share]);
    }
}

