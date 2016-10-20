import { NgModule } from '@angular/core';
import { CommonModule} from '@angular/common';
import { RouterModule } from '@angular/router';

import { HoldingsMDComponent } from './HoldingsMD.component';

@NgModule({
    imports: [RouterModule, CommonModule],
    declarations: [HoldingsMDComponent],
    exports: [HoldingsMDComponent]
})

export class HoldingsMDModule { }
