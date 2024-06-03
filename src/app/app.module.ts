import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';

//componenti 
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { RegistrationComponent } from './registration/registration.component';
import { SearchComponent } from './search/search.component';
import { IaComponent } from './ia/ia.component';
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
        AppRoutingModule
    ],
    providers: [],
    bootstrap: []
})
export class AppModule {}
