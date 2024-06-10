import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
//componenti
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { RegistrationComponent } from './registration/registration.component';
import { IaComponent } from './ia/ia.component';
import { SearchComponent } from './search/search.component';
const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'login', component: LoginComponent },
  { path: 'registration', component: RegistrationComponent },
  { path: 'search', component: SearchComponent },
  { path: 'ia', component: IaComponent },
  { path: '', redirectTo: '/home', pathMatch: 'full'} // Gestione degli URL non validi
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }