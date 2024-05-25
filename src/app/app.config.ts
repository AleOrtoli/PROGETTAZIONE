import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { Routes } from '@angular/router';
//componenti
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { RegistrationComponent } from './registration/registration.component';
import { SearchComponent } from './search/search.component';
import { IaComponent } from './ia/ia.component';
import { HttpClientModule } from '@angular/common/http';
import { importProvidersFrom } from '@angular/core';



const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'registration', component: RegistrationComponent },
  { path: 'login', component: LoginComponent },
  { path: 'search', component: SearchComponent },
  { path: 'ia', component: IaComponent },
  { path: '', component: HomeComponent }, // Redireziona alla pagina 1 di default
  { path: '**', redirectTo: '/page1' } // Gestione degli URL non validi
];export const appConfig: ApplicationConfig = {
  providers: [provideRouter(routes), 
          importProvidersFrom(HttpClientModule)]
};