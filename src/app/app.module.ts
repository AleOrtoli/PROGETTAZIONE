import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';

//componenti 
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { RegistrationComponent } from './registration/registration.component';
import { SearchComponent } from './search/search.component';
import { IaComponent } from './ia/ia.component';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
@NgModule({
    declarations: [
    ],
    imports: [
        //componenti
        IaComponent,
        SearchComponent,
        RegistrationComponent,
        LoginComponent,
        HomeComponent,
        //collegamenti
        AppRoutingModule,
        RouterModule,
        CommonModule

    ],
    providers: [],
    bootstrap: []
})
export class AppModule {}
