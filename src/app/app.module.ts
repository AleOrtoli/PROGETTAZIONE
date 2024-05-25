import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RouterModule, Routes} from '@angular/router';
import { RouterOutlet } from '@angular/router';

import { CommonModule } from '@angular/common'; // Importa CommonModule
import { HttpClientModule, provideHttpClient, HttpClientXsrfModule } from '@angular/common/http';

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
        AppComponent,
        //componenti
        IaComponent,
        SearchComponent,
        RegistrationComponent,
        LoginComponent,
        HomeComponent,
        //collegamenti
        BrowserModule,
        AppRoutingModule,
        RouterModule,
        RouterOutlet,
        //server
        HttpClientModule,
        CommonModule,
        HttpClientXsrfModule.withOptions({
            cookieName: 'My-Xsrf-Cookie',
            headerName: 'My-Xsrf-Header',
          })
    ],
    providers: [],
    bootstrap: []
})
export class AppModule { }
