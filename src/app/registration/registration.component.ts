import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import {NgForm} from '@angular/forms';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms'; 
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-registration',
  standalone: true,
  imports: [RouterModule, CommonModule, FormsModule
  ],
  templateUrl: './registration.component.html',
  styleUrl: './registration.component.css',
  
}) 
export class RegistrationComponent {
  RegistrationSuccess : String = '';
  RegistrationFailed : String = '';
  private apiUrl = 'http://localhost:5001/registration';

  constructor(private http: HttpClient) {}

  onRegister(registerForm: NgForm) {
    if (registerForm.valid) {
      this.http.post<any>(this.apiUrl, registerForm.value).subscribe(
        response => {
          console.log('User registered successfully:', response);
          this.RegistrationSuccess = 'Registrazione avvenuta con successo.';
        },
        error => {
          console.error('Error during registration:', error);
          if (error.error && error.error.error) {
            this.RegistrationFailed = error.error.error;
          } else {
            this.RegistrationFailed = 'Registrazione fallita';
          }
        }
         // Verifica se l'errore contiene un messaggio specifico dal backend
        
      );
    } else {
      console.log('Form is invalid');
    }
  }
}
