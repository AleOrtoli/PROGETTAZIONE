import { RouterModule } from '@angular/router';
import { Component } from '@angular/core';
import {NgForm} from '@angular/forms';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms'; 
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [RouterModule, CommonModule, FormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  loginError: string = '';
  private apiUrl = 'http://localhost:5000/login'; 
  
  constructor(private http: HttpClient) { }

  onLogin(loginForm: NgForm): void {
    if (loginForm.valid) {
      this.http.post<any>(this.apiUrl, loginForm.value ).subscribe(
        response => {
          console.log('success:', response);
          // Qui puoi aggiungere la logica per gestire una registrazione avvenuta con successo
        },
        error => {
          console.error('Error during login:', error);
          
          this.loginError = 'Credenziali di accesso errate. Riprova.';
        }
      );
    } else {
      console.log('Form is invalid');
    }
  }
}
